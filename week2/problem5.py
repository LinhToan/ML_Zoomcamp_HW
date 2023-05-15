# Question 5: Given list of seeds, calculate the standard deviation of all the scores.
import pandas as pd
import numpy as np

def prepare_X(df, fill_nulls):
    '''Filles in null values'''
    df_num = df
    df_num = df_num.fillna(fill_nulls)
    X = df_num.values
    return X
 
def train_lin_reg(X, y):
    '''Linear regression function from lessons'''
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

def rmse(y, y_pred):
    '''Root mean squared error function from lessons'''
    error = y - y_pred
    se = error ** 2
    mse = se.mean()
    return np.sqrt(mse)

def solution(df, seed_list):
    '''Calculates the standard deviation of the given seed list'''
    
    base = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
    df = df[base]

    # Create split for training, validation, testing distribution.
    n = len(df)

    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    scores = []
    for seed in seed_list:
        # Create variables to shuffle data set, using seeds from the list given.
        idx = np.arange(n)
        np.random.seed(seed)
        np.random.shuffle(idx)

        # Split the original dataset into training, validation, and testing sets.
        df_train = df.iloc[idx[:n_train]].copy()
        df_val = df.iloc[idx[n_train:n_train + n_val]].copy()
        df_test = df.iloc[idx[n_train + n_val:]].copy()

        # Reset index for each data set.
        df_train = df_train.reset_index(drop=True)
        df_val = df_val.reset_index(drop=True)
        df_test = df_test.reset_index(drop=True)

        # Create target variable for data sets.
        y_train = np.log1p(df_train.median_house_value.values)
        y_val = np.log1p(df_val.median_house_value.values)
        y_test = np.log1p(df_test.median_house_value.values)

        # Remove target variable from data sets.
        del df_train['median_house_value']
        del df_val['median_house_value']
        del df_test['median_house_value']
    
        # Fill in missing values with 0 in validation dataset
        X_train = prepare_X(df_train, fill_nulls=0)
        w0, w = train_lin_reg(X_train, y_train)

        # Validate dataset with testing dataset
        X_val = prepare_X(df_val, fill_nulls=0)
        y_pred = w0 + X_val.dot(w)

        # Compute root mean squared error
        rmse_vals = np.round(rmse(y_val, y_pred), 2)
        scores.append(rmse_vals)

    return np.std(scores).round(3)