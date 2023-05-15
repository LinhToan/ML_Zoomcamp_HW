#Question 3: Train a linear regression model and compute the RMSE value.
import pandas as pd
import numpy as np

def prepare_X(df, fill_nulls):
    '''Filles in null values'''
    df_num = df
    df_num = df_num.fillna(fill_nulls)
    X = df_num.values
    return X

def train_lin_reg(X, y):
    
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

def solution(df):
    '''Computes RMSE value'''

    base = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
    df = df[base]
    
    # Create split for training, validation, testing distribution.
    n = len(df)

    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    # Create variables to shuffle data set, using seed = 42.
    idx = np.arange(n)
    np.random.seed(42)
    np.random.shuffle(idx)

    # Split the original dataset into training, validation, and testing sets.
    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

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

    # Fill in missing values with 0 and train dataset
    df_train_zeroes = prepare_X(df_train, 0)
    w0_zeroes, w_zeroes = train_lin_reg(df_train_zeroes, y_train)

    # Validate dataset
    X_val_zeroes = prepare_X(df_val, 0)
    y_pred_zeroes = w0_zeroes + X_val_zeroes.dot(w_zeroes)

    # Compute root mean squared error
    return rmse(y_val, y_pred_zeroes).round(3)
    # RMSE is 0.330