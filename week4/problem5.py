# Use the KFold class from Scikit-Learn to evaluate our model on 5 different folds.
# How large is the standard deviation of the AUC scores across different folds?
# - 0.003
# - 0.014
# - 0.09
# - 0.24

from prepare_data import prepare
from split_data import split_dataset
from log_reg import log_reg_model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

def solution(df, columns, kfold):
    '''Evaluates our logistic regression model using KFold across 5 different folds.'''

    df_prepared = prepare(df)
    # df_train, df_val, df_test, y_train, y_val, y_test = split_dataset(df_prepared)
    # y_pred = log_reg_model(cols, df_train, df_val, y_train, y_val)

    df_full_train, df_test = train_test_split(df_prepared, test_size=0.2, random_state=1)

    df_full_train = df_full_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    scores = []

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
    
    for train_idx, val_idx in kfold.split(df_full_train):
        df_train = df_full_train.iloc[train_idx]
        df_val = df_full_train.iloc[val_idx]
        
        y_train = df_train.card.values
        y_val = df_val.card.values
        
        dv, model = train(df_train, y_train, 1.0)
        y_pred = predict(df_val, dv, model)
        
        auc = roc_auc_score(y_val, y_pred)
        scores.append(auc)
        
    ans = 'The mean and std of the AUC across different folds are %.3f +- %.3f' % (np.mean(scores), np.std(scores))
    return ans