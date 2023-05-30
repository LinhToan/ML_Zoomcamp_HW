from sklearn.model_selection import train_test_split

def split_dataset(df):
    '''Splits dataset into train/validation/testing with a 60/20/20 distribution'''
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train.card.values
    y_val = df_val.card.values
    y_test = df_test.card.values

    del df_train['card']
    del df_val['card']
    del df_test['card']

    return df_train, df_val, df_test, y_train, y_val, y_test