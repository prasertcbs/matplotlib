# data source: http://popcensus.nso.go.th/pop_data/2553/3/whole_kingdom/Table3.xls
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
age = np.array(
    ["0 - 4", "5 - 9", "10 - 14", "15 - 19", "20 - 24", "25 - 29", "30 - 34", "35 - 39",
     "40 - 44", "45 - 49", "50 - 54", "55 - 59", "60 - 64", "65 - 69", "70 - 74",
     "75 - 79", "80 - 84", "85 - 89", "90 - 94", "95 - 99", "> 100"])
m = np.array(
    [1915887, 2100931, 2494484, 2464805, 2361297, 2529633, 2669927, 2754129, 2753282,
     2552531, 2211649, 1697221, 1311024, 902675, 722246, 482686, 273915, 108639, 35867,
     10965, 1238])
f = np.array(
    [1823981, 1980712, 2369795, 2435784, 2330223, 2562964, 2724990, 2860720, 2918730,
     2713534, 2376384, 1869867, 1454373, 1030677, 885393, 640698, 388748, 172302, 64170,
     19868, 2711])
x = np.arange(age.size)
m_total = np.sum(m)
f_total = np.sum(f)
def fmt_million(val, pos):
    return "{:.1f}M".format(np.abs(val) / 1000000)

def plot_pyramid():
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(FuncFormatter(fmt_million))
    ax.set_xlim(-3e6,3e6)
    for i in range(m.size):
        plt.text(100000, i, "{:.1f}M ({:.1f}%)".format(f[i] / 1e6, f[i]*100/f_total), fontsize=6, verticalalignment="center")
        plt.text(-100000, i, "{:.1f}M ({:.1f}%)".format(m[i] / 1e6, m[i]*100/m_total), fontsize=6, verticalalignment="center", horizontalalignment="right")

    plt.barh(x, -m, alpha=.5, height=.95, color="deepskyblue")
    plt.barh(x, f, alpha=.5, height=.95, color="pink")
    plt.yticks(x, age)
    plt.title("Population by age groups, gender")
    plt.show()


if __name__ == '__main__':
    plot_pyramid()
