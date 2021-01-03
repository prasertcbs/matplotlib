import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data  # 0.19


def demo():
    s = ["SCC.BK", "PTT.BK", "bbl.bk", "aot.bk", "bh.bk", "kbank.bk", "cpf.bk", "dtac.bk"]
    fig, ax = plt.subplots(2, 4)
    print(ax.shape)
    stocks = np.array(s).reshape(ax.shape)
    print(stocks.shape)
    start_dt = "2017-1-1"
    end_dt = "2017-1-31"
    for r in range(ax.shape[0]):
        for c in range(ax.shape[1]):
            df = data.DataReader(stocks[r, c], data_source="yahoo", start=start_dt,
                                 end=end_dt)
            # print(df.head())
            a = ax[r, c]
            a.set_title(stocks[r, c])
            a.plot(df["Adj Close"])
            a.tick_params(axis="both", which="major", labelsize=7, color=".7")
            a.spines["left"].set_color(".7")
            a.spines["bottom"].set_color(".7")
            a.spines["top"].set_color("white")
            a.spines["right"].set_color("white")
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    demo()
