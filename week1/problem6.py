# Question 6:
import pandas as pd

<<<<<<< HEAD
def solutionA(df):
=======
def solution1(df):
>>>>>>> main
    """Part 1: Find the median value of 'Engine Cylinders' column in the dataset."""
    return df['Engine Cylinders'].median()
    # The median value of "Engine Cylinders" is 6

<<<<<<< HEAD
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
=======
def solution2(df):
    """Part 2: Calculate the most frequent value of 'Engine Cylinders'"""
    mode_engine_cyl = df['Engine Cylinders'].mode()[0]
    return mode_engine_cyl
    # The mode value is 4

def solution3(df):
    """Part 3: Use the 'fillna' method to fill the missing values in 'Engine Cylinders' 
       with the most frequent value from the previous step."""
    mode = solution2(df)
    df['Engine Cylinders'] = df['Engine Cylinders'].fillna(mode)
    return (df['Engine Cylinders'].isnull().sum() != 0).sum()

def solution4(df):
    """part 4: Calculate the median value of 'Engine Cylinders' again. Has it changed?"""
>>>>>>> main
    return df['Engine Cylinders'].median()
    # No, the median has not changed