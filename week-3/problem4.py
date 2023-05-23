# Question 4: Now let's train a logistic regression. Remember that we have one categorical variable ocean_proxmity
# in the data. Include it using one-hot encoding. Fit the model on the training dataset.
# Calculate the accuracy on the validation dataset and round it to 2 decimal digits. Options:
# 0.60
# 0.72
# 0.84
# 0.95

from prepare_data import prepare
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def solution(df):
    '''Trains a logistic regression model on the training dataset, then calculates its accuracy score.'''
    df_prepared = prepare(df)

    house_value_mean = df_prepared.median_house_value.mean()
    df_prepared['above_average'] = df_prepared.median_house_value.map(lambda x: int(x > house_value_mean))

    df_log_reg = df_prepared.copy()
    del df_log_reg['median_house_value']

    df_full_train, df_test = train_test_split(df_log_reg, test_size=0.2, random_state=42)
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

    model = LogisticRegression(solver="liblinear", C=1.0, max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    val_dicts = df_val.to_dict(orient='records')
    X_val = dv.transform(val_dicts)
    y_pred = model.predict(X_val)

    accuracy = round(accuracy_score(y_val, y_pred), 2)

    return accuracy
    # Accuracy should be 0.84