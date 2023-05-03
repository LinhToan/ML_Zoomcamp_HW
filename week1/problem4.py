# Question 4: What's the number of unique Audi car models in the dataset?
import pandas as pd

def solution(df):
    return df[df['Make'] == 'Audi']['Model'].nunique()
    # 34 unique Audi car models