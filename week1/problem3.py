# Question 3: Who are the most frequent car manufacturers (top-3) according to the dataset?
import pandas as pd

def solution(df):
    return df.Make.value_counts().head(3).to_dict()
    # Top 3 most frequent car manufacturers are Chevrolet, Ford, and Volkswagen.
