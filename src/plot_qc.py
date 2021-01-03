import numpy as np
import matplotlib.pyplot as plt


def qc_plot():
    n = 100
    x = np.arange(n)
    d = np.random.normal(150, 5, n)
    m, sd = np.mean(d), np.std(d)
    # plt.hist(d, 30, normed=True)
    plt.plot(x, d, marker="o", color=".7", alpha=.7)
    filter = np.where((d > m + 2 * sd) | (d < m - 2 * sd))
    plt.plot(x[filter], d[filter], marker="o", color="pink", linestyle="")

    plt.axhline(m, color="green", linestyle="--")
    # t = "n = {}, mean = {:.2f}, sd = {:.2f}".format(n, m, sd)
    t = "n = {}, {} = {:.2f}, sd = {:.2f}".format(n, r"$\bar{x}$", m, sd)
    plt.title(t)
    plt.ylabel("weight (grams)")
    ucl = 2 * sd
    lcl = -ucl
    plt.axhline(m + ucl, color="red", linestyle="--")
    plt.axhline(m + lcl, color="red", linestyle="--")

    plt.show()


def qc_band_plot():
    n = 100
    x = np.arange(n)
    d = np.random.normal(150, 5, n)
    m, sd = np.mean(d), np.std(d)
    # plt.hist(d, 30, normed=True)
    plt.plot(x, d, marker="o", color=".7", alpha=.7, linestyle="")
    filter = np.where((d > m + 2 * sd) | (d < m - 2 * sd))
    plt.plot(x[filter], d[filter], marker="o", color="red", linestyle="")

    plt.axhline(m, color="green", linestyle="--")
    # t = "n = {}, mean = {:.2f}, sd = {:.2f}".format(n, m, sd)
    t = "n = {}, {} = {:.2f}, sd = {:.2f}".format(n, r"$\bar{x}$", m, sd)
    plt.title(t)
    plt.ylabel("weight (grams)")
    ucl = 2 * sd
    lcl = -ucl
    plt.fill_between(x, m + ucl, m + 5 * sd, alpha=.1, color="red")
    plt.fill_between(x, m + lcl, m - 5 * sd, alpha=.1, color="red")
    # plt.axhline(m+ucl, color="red", linestyle="--")
    # plt.axhline(m+lcl, color="red", linestyle="--")
    plt.show()


if __name__ == '__main__':
    # qc_plot()
    qc_band_plot()
