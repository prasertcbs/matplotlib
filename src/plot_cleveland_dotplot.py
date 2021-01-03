import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demo():
    df = pd.read_csv("mtcars.csv")
    df.sort_values("mpg", inplace=True)
    print(df.head())
    x = np.arange(df.model.size)
    y = df.mpg * 0.425144 # convert miles/gallon to kilos/litre

    fig, ax = plt.subplots()
    plt.barh(x, y, height=.1, color=".9", zorder=-1)
    plt.yticks(x, df.model, fontsize=6)
    plt.scatter(y, x, color="yellow")
    plt.scatter(y[y >= 12], x[y >= 12], color="green")
    plt.scatter(y[y < 8], x[y < 8], color="red")
    plt.axvline(x=12, color="green", alpha=.5, linestyle="--")
    plt.axvline(x=8, color="red", alpha=.5, linestyle="--")
    plt.xlabel("kilometre per litre")
    plt.title("Fuel efficiency")
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    demo()
