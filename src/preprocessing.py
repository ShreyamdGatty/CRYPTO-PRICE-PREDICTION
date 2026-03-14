def clean_data(df):

    df = df.dropna()

    df = df.sort_values("date")

    return df
