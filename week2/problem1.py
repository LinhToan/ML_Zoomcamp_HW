# Question 1: Find a feature with missing values. How many missing values does it have?
import pandas as pd

def solution(df):
    base = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
    df = df[base]
    return df.isnull().sum().sum()
    # There are 207 missing values