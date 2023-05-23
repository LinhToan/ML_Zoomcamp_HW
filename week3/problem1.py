# Question 1: Fill in missing values, create new columns, 
# and find out what the most frequent observation (mode) for the column 'ocean_proximity'

from prepare_data import prepare

def solution(df):
    '''This function returns the mode of ocean_proximity'''
    df_prepared = prepare(df)
    return df_prepared.ocean_proximity.mode()[0]
    # Answer is '<1h_ocean'