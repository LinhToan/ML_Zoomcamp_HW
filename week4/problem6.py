# Question 6: Now let's use 5-fold cross-validation to find the best parameter C, using
# C values of [0.01, 0.1, 1, 10]. Initialize KFold with the same parameters as Q5 
# and compute the mean and std rounded to 3 decimal digits.

from prepare_data import prepare
from split_data import split_dataset
from log_reg import log_reg_model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import KFold

def solution(df, c_list, columns):
    '''Calculates the best C parameter from a given list for 5-fold cross-validation.'''
    df_prepared = prepare(df)
    # df_train, df_val, df_test, y_train, y_val, y_test = split_dataset(df_prepared)
    # y_pred = log_reg_model(cols, df_train, df_val, y_train, y_val)

    df_full_train, df_test = train_test_split(df_prepared, test_size=0.2, random_state=1)

    df_full_train = df_full_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    def train(df, y, c):   
        dicts = df[columns].to_dict(orient='records')
        
        dv = DictVectorizer(sparse=False)
        X_train = dv.fit_transform(dicts)
        
        model = LogisticRegression(solver='liblinear', C=c, max_iter=1000)
        model.fit(X_train, y)
        
        return dv, model

    def predict(df, dv, model):
        dicts = df[columns].to_dict(orient='records')
        
        X = dv.transform(dicts)
        y_pred = model.predict_proba(X)[:, 1]
        
        return y_pred

    c_dict = {}

    for C in c_list:
        kfold = KFold(n_splits=5, shuffle=True, random_state=1)

        scores = []

        for train_idx, val_idx in kfold.split(df_full_train):
            df_train = df_full_train.iloc[train_idx]
            df_val = df_full_train.iloc[val_idx]

            y_train = df_train.card.values
            y_val = df_val.card.values

            dv, model = train(df_train, y_train, C)
            y_pred = predict(df_val, dv, model)

            auc = roc_auc_score(y_val, y_pred)
            scores.append(auc)

        c_dict[C] = [np.mean(scores).round(3), np.std(scores).round(3)]

    max_mean = max(i for v in c_dict.values() for i in v)
    min_std = min([k[1] for k in c_dict.values() if max_mean in k])
    min_c = min([k for k,v in c_dict.items() if v == [max_mean, min_std]])

    ans = f'C={min_c} gives us a mean and std of {max_mean} +- {min_std}'

    return ans