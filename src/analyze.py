from collections import Counter

def top_actors(df, top_n=10):
    all_actors =[]
    for actors in df["cast_list"]:
        all_actors.extend(actors)
    counter = Counter(all_actors)
    return counter.most_common(top_n)

def stats(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isna().sum().to_dict()
    }