# Question 6: Given a list of alpha values [0, 0.01, 0.1, 1 10], calcualte which one leads to the
# best RMSE on the validation set. Round your RMSE score to 3 decimal digits.
# If there are multiple options, then select the smallest alpha.

from prepare_data import prepare
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def solution(df):
    '''Given the list of alpha parameters in the prompt, we determine which one yields the lowest RMSE score on the validation dataset'''
    df_prepared = prepare(df)

    house_value_mean = df_prepared.median_house_value.mean()
    df_prepared['above_average'] = df_prepared.median_house_value.map(lambda x: int(x > house_value_mean))

    df_ridge = df_prepared.copy()
    df_ridge.median_house_value = np.log1p(df_ridge.median_house_value)
    a = [0, 0.01, 0.1, 1, 10]
    a_dict = {}
    
    # Split the dataset into training-validation-testing sets
    df_full_train, df_test = train_test_split(df_ridge, test_size=0.2, random_state=42)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train.above_average.values
    y_val = df_val.above_average.values
    y_test = df_test.above_average.values

    del df_train['above_average']
    del df_val['above_average']
    del df_test['above_average']    

    dv = DictVectorizer(sparse=False)
    train_dicts = df_train.to_dict(orient='records')
    X_train = dv.fit_transform(train_dicts)
    val_dicts = df_val.to_dict(orient='records')
    X_val = dv.transform(val_dicts)
        
    # Test each number in a to find the best RMSE for our ridge regression model
    for num in a:
        model = Ridge(alpha=num, solver='sag', random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        rmse_val = round(mean_squared_error(y_test, y_pred, squared=False), 3)
        a_dict[num] = rmse_val
        # print(f'The "a" value of {num} gives an RMSE of {rmse_val}')
        
    min_key = min(a_dict, key=a_dict.get)
    min_value = a_dict[min_key]
    ans = 'The smallest "a" value is {} and gives us a RMSE of {}'.format(min_key, min_value)
    return ans
    # The smallest "a" value is 0 and gives us a RMSE of 0.517