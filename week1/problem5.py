# Question 5: How many columns in the dataset have missing values?
import pandas as pd

def solution(df):
    return (df.isnull().sum() != 0).sum()
    # There are 5 columns with missing values