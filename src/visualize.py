import matplotlib.pyplot as plt
from pathlib import Path

def plot_hist(df,column):
    Path("reporst/figures").mkdir(parents=True, exist_ok=True)
    df[column].hist()
    plt.savefig("reports/figures/hist.png")
    plt.close()

def plot_top_actors(top_list):
    names = [x[0] for x in top_list]
    counts = [x[1] for x in top_list]
    plt.figure(figsize=(10,6))
    plt.barh(names, counts)
    plt.gca().invert_yaxis()
    plt.title("Top 10 najczęsciej występujących aktorów")
    plt.xlabel("Liczba wystąpień")

    Path("reports/figures").mkdir(parents=True, exist_ok=True)
    plt.savefig("reports/figures/top_actors.png")
    plt.close() 