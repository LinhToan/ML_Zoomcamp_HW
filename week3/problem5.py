# Question 5: Use the feature elimination technique to eliminate the least useful feature.
# Train a model with all features using the same parameters as in Q4. Now exclude each feature
# from this set and train a model without it. Record the accuracy for each model.
# For each feature, calculate the difference between the original accuracy and
# the accuracy without the feature. Which of the following as the smallest difference?
# total_rooms
# total_bedrooms
# population
# households

from prepare_data import prepare
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def solution(df):
    '''Performs the feature elimination technique on the dataset.'''
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

    features_list = df_train.columns.values.tolist()
    min_diff = {}
    feat = {'total_rooms': 1, 'total_bedrooms': 1, 'population': 1, 'bedrooms': 1}

    for f in features_list:
        features_test = features_list.copy()
        features_test.remove(f)
        
        dv = DictVectorizer(sparse=False)
        train_dicts = df_train[features_test].to_dict(orient='records')
        X_train = dv.fit_transform(train_dicts)
        
        model = LogisticRegression(solver="liblinear", C=1.0, max_iter=1000, random_state=42)
        model.fit(X_train, y_train)
        
        val_dicts = df_val[features_list].to_dict(orient='records')
        X_val = dv.transform(val_dicts)
        y_pred = model.predict(X_val)
        
        score = round(accuracy_score(y_val, y_pred), 2)
        
        if f in feat.keys():
            min_diff[f] = round(accuracy - score, 2)
        
        # print(f'For {f}, the difference is {round(accuracy - score, 2)} and accuracy score is {score}')
        
    min_key = min(min_diff, key=min_diff.get)
    min_value = min_diff[min_key]

    ans = 'The feature with the smallest difference is {} with a difference of {}'.format(min_key, min_value)
    return ans
    # The feature with the smallest difference is total_rooms with a difference of 0.0