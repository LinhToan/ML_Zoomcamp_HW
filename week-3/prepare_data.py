def prepare(df):
    '''This function prepares the dataframe for question 1.'''
    # Change categorical column names to lower case.
    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    # From exploring the data in our Jupyter notebook, we see that total_bedrooms has 207 null values.
    bedroom_median = df.total_bedrooms.median()
    df = df.fillna(bedroom_median)

    df['rooms_per_household'] = df.total_rooms / df.households
    df['bedrooms_per_room'] = df.total_bedrooms / df.total_rooms
    df['population_per_household'] = df.population / df.households

    return df