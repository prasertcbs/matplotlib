import pandas as pd
from pandas_datareader import data


def basic():
    df = data.DataReader("PTT.BK", data_source="yahoo",
                         start="2017-1-1", end="2017-1-31")
    print(df.head())
    df.to_csv("ptt.csv")
    # wb = pd.ExcelWriter("ptt.xlsx", engine="xlsxwriter")
    # df.to_excel(wb, "ptt2017")
    # wb.save()


def n_stock():
    stocks = ["PTT.BK", "SCC.BK", "BBL.bk", "cpf.bk"]
    fname = "stocks5.csv"
    start_dt = "2017-1-1"
    end_dt = "2017-1-10"
    for i, s in enumerate(stocks):
        df = data.DataReader(s, data_source="yahoo",
                             start=start_dt, end=end_dt)
        df["Symbol"] = s
        with open(fname, "a") as f:
            df.to_csv(f, header=True if i == 0 else False)


def n_stock2(stocks, start_dt, end_dt, fname="mystock.csv"):
    # stocks = ["PTT.BK", "SCC.BK", "BBL.bk", "cpf.bk"]
    # start_dt = "2017-1-1"
    # end_dt = "2017-1-10"
    # fname = "stocks99.csv"
    for i, s in enumerate(stocks):
        df = data.DataReader(s, data_source="yahoo",
                             start=start_dt, end=end_dt)
        df["Symbol"] = s
        with open(fname, "a") as f:
            df.to_csv(f, header=True if i == 0 else False)


def read_stock_list(fname="stock_list.txt"):
    with open(fname, newline="") as f:
        s = f.readlines()
    return [_.rstrip() for _ in s]


if __name__ == '__main__':
    # basic()
    # n_stock()
    l = read_stock_list()
    # print(l)
    n_stock2(l, '2016-1-1', '2016-1-7')
