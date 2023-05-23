# Question 3: Calculate the mutual information score between above_average and ocean_proxmity. 
# Use the training set only and round it to 2 decimals.
# What is their mutual information score?
# 0.26
# 0
# 0.10
# 0.16

from prepare_data import prepare
from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score

def solution(df):
    '''Calculates the mutual information score between above_average and ocean_proximity'''
    df_prepared = prepare(df)

    # Make median_house_value binary
    house_value_mean = df_prepared.median_house_value.mean()
    df_prepared['above_average'] = df_prepared.median_house_value.map(lambda x: int(x > house_value_mean))
    
    #Split the data
    df_log_reg = df_prepared.copy()
    del df_log_reg['median_house_value']

    df_full_train, df_test = train_test_split(df_log_reg, test_size=0.2, random_state=42)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train.above_average.values
    y_val = df_val.above_average.values
    y_test = df_test.above_average.values

    score = mutual_info_score(df_train.above_average, df_train.ocean_proximity).round(2)
    return score
    # Mutual info score between above_average and ocean_proxmity is 0.10