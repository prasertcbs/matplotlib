import matplotlib.pyplot as plt
import numpy as np


def demo1():
    fig = plt.figure()
    ax1 = plt.subplot2grid((2, 5), (0, 0), rowspan=1, colspan=3)
    ax2 = plt.subplot2grid((2, 5), (0, 3), rowspan=1, colspan=2)
    ax3 = plt.subplot2grid((2, 5), (1, 0), rowspan=1, colspan=5)
    plt.show()


def demo2():
    fig = plt.figure()
    ax1 = plt.subplot2grid((2, 6), (0, 0), rowspan=2, colspan=4)
    ax2 = plt.subplot2grid((2, 6), (0, 4), rowspan=1, colspan=2)
    ax3 = plt.subplot2grid((2, 6), (1, 4), rowspan=1, colspan=2)
    x = np.arange(6)
    ax1.plot(x, np.random.randint(1, 11, x.size))
    ax2.bar(x, np.random.randint(1, 11, x.size), color="orange")
    ax3.scatter(x, np.random.randint(1, 11, x.size), color="red")
    ax1.set_title("line")
    ax2.set_title("bar")
    ax3.set_title("scatter")
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    # demo1()
    demo2()
