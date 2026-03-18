def clean(df):
    df = df.dropna()
    return df

def add_cast_count(df):
    df["cast_count"] = df["cast"].apply(lambda x: len(x.split(",")))
    return df

def explode_cast(df):
    df["cast_list"] = df["cast"].apply(lambda x: [name.strip() for name in x.split(",")])
    return df