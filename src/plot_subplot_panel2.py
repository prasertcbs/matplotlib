import matplotlib.pyplot as plt
import numpy as np


def demo2():
    fig, ax = plt.subplots(2, 1)
    # print(ax)
    # print(type(ax))
    # print(ax.shape)
    ax[0].plot([3, 7, 5, 1])
    ax[1].bar(range(4), [3, 7, 5, 1])
    plt.show()


def demo3():
    fig, ax = plt.subplots(2, 3, sharex=True, sharey=True)
    # print(ax)
    # print(type(ax))
    print(ax.shape)
    for r in range(ax.shape[0]):
        for c in range(ax.shape[1]):
            ax[r, c].plot(np.random.randint(1, 11, 5))
            ax[r, c].set_title("ax[{},{}]".format(r, c))
    plt.show()


if __name__ == '__main__':
    # demo2()
    demo3()
