# Question 2: Create the correlation matrix for the numerical features of your train dataset.
# In a correlation matrix, you compute the correlation coefficient between every pair of features in the dataset.
# What are the two features that have the biggest correlation in this dataset? Options:
# total_bedrooms and households
# total_bedrooms and total_rooms
# population and households
# population_per_household and total_rooms

from prepare_data import prepare

def solution(df_original):
    '''Computes the correlation between the features given above in the prompt.'''
    df_numerical = prepare(df_original).drop(columns=['ocean_proximity', 'median_house_value'])

    # Since we were given options for answers in the prompt, we will just compute the correlation values
    # of each pair of features and return the highest value.
    corr_dict = {}
    corr_dict['total bedrooms and households'] = df_numerical.corrwith(df_original.households).total_bedrooms
    corr_dict['total bedrooms and total_rooms'] = df_numerical.corrwith(df_original.total_rooms).total_bedrooms
    corr_dict['population and households'] = df_numerical.corrwith(df_original.households).population
    corr_dict['population_per_household and total rooms'] = df_numerical.corrwith(df_original.total_rooms).population_per_household

    max_features = max(corr_dict, key=corr_dict.get)
    max_corr = corr_dict[max_features].round(3)
    ans = 'The features with the highest correlation are {} with a correlation value of {}'.format(max_features, max_corr)
    return ans