import pandas as pd

def prepare(df):
    '''Create the target variable by mapping yes to 1 and no to 0.'''
    df['card'] = df['card'].map(lambda x: int(x == 'yes'))

    return df
