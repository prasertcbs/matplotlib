import numpy as np
import matplotlib.pyplot as plt


def heart():
    # http://mathworld.wolfram.com/HeartCurve.html
    t = np.linspace(0, 2 * np.pi, 360)
    # print(t)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    plt.plot(x, y)
    plt.plot(x + 10, y)
    plt.plot(x + 20, y)
    plt.show()


def heart2():
    # http://mathworld.wolfram.com/HeartCurve.html
    t = np.linspace(0, 2 * np.pi, 360)
    # print(t)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    r = np.linspace(.1, 1, 10)
    plt.text(0, 0, "I \u2764 Python")

    for n in r:
        # plt.plot(x + n, y)
        # plt.plot(x * n, y)
        # plt.plot(x * n / 5, y)
        plt.plot(x * n / 5, y * n / 5)
    plt.show()


if __name__ == '__main__':
    # heart()
    heart2()
