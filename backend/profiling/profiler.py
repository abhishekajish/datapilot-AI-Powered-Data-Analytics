def generate_profile(df):

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicates": df.duplicated().sum(),
        "missing_values": df.isnull().sum(),
        "data_types": df.dtypes
    }

    return profile