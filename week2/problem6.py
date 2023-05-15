# Question 6: For a seed of 9, train a linear regression model and calculate the RMSE.
import pandas as pd
import numpy as np

def prepare_X(df, fill_nulls):
    '''Filles in null values'''
    df_num = df
    df_num = df_num.fillna(fill_nulls)
    X = df_num.values
    return X
 
def train_lin_reg_regularized(X, y, r):
    '''Regularized linear regression function from lessons'''
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    XTX = XTX + r * np.eye(XTX.shape[0])
    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

def rmse(y, y_pred):
    '''Root mean squared error function from lessons'''
    error = y - y_pred
    se = error ** 2
    mse = se.mean()
    return np.sqrt(mse)

def solution(df, seed):
    '''Given a dataframe and seed, this function calculates the RMSE value'''

    base = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
    df = df[base]

    # Create split for training, validation, testing distribution.
    n = len(df)

    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test
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
    
    # Combine the training and validation datasets
    df_full_train = pd.concat([df_train, df_val])
    df_full_train = df_full_train.reset_index(drop=True)
    y_full_train = np.concatenate([y_train, y_val])
    
    # Fill in missing values with 0 in full train dataset
    X_full_train = prepare_X(df_full_train, fill_nulls=0)
    w0, w = train_lin_reg_regularized(X_full_train, y_full_train, r=0.001)

    # Validate dataset with testing dataset
    X_test = prepare_X(df_test, fill_nulls=0)
    y_pred = w0 + X_test.dot(w)

    # Compute root mean squared error
    rmse_val = np.round(rmse(y_test, y_pred), 2)

    return rmse_val