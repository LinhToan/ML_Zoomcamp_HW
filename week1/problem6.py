# Question 6:
import pandas as pd

def solutionA(df):
    """Part 1: Find the median value of 'Engine Cylinders' column in the dataset."""
    return df['Engine Cylinders'].median()
    # The median value of "Engine Cylinders" is 6

def solutionB(df):
    """Part 2: Calculate the most frequent value of 'Engine Cylinders'"""
    return df['Engine Cylinders'].mode()[0]
    # The mode value is 4

def solutionC(df):
    """Part 3: Use the 'fillna' method to fill the missing values in 'Engine Cylinders' 
       with the most frequent value from the previous step.
       Part 4: Calculate the median value of 'Engine Cylinders' again. Has it changed?"""
    mode = solutionB(df)
    df['Engine Cylinders'] = df['Engine Cylinders'].fillna(mode)
    return df['Engine Cylinders'].median()
    # No, the median has not changed
