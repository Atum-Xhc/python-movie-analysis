from src.load_data import load_csv
from src.clean_data import clean, add_cast_count, explode_cast
from src.analyze import stats, top_actors
from src.visualize import plot_hist, plot_top_actors

def main():
    df = load_csv("data/raw/dane.csv")
    df = clean(df)
    df = add_cast_count(df) 
    df = explode_cast(df)

    print(stats(df))
    top10 = top_actors(df)
    print(top10)
    plot_top_actors(top10)
    

if __name__ == "__main__":
    main()
