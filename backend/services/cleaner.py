def clean_data(df):

    original_rows = df.shape[0]

    # Remove duplicate rows
    df = df.drop_duplicates()

    duplicates_removed = original_rows - df.shape[0]

    # Fill missing numeric values with median
    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    return df, duplicates_removed