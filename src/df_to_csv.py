import pandas as pd
from pandas_datareader import data


def basic():
    df = data.DataReader("PTT.BK", data_source="yahoo",
                         start="2017-1-1", end="2017-1-31")
    print(df.head())
    # df.to_csv("ptt.csv")
    wb = pd.ExcelWriter("ptt.xlsx", engine="xlsxwriter")
    df.to_excel(wb, "ptt2017")
    wb.save()


if __name__ == '__main__':
    basic()
