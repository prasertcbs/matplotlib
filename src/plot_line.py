import matplotlib.pyplot as plt


def demo():
    plt.plot([20, 15, 32], color="pink", marker="o")
    plt.plot([25, 35, 12], color="green", linestyle="--")
    plt.show()


def demo2():
    plt.plot([2014, 2015, 2016], [20, 15, 32], color="pink", marker="o")
    plt.plot(range(2014, 2017), [25, 35, 12], color="green", linestyle="--")
    plt.show()


def demo3():
    x = range(2014, 2021)
    y = [20, 25, 18, 15, 17, 20, 22]
    plt.plot(x, y)
    plt.show()


def demo4():
    x = range(2014, 2021)
    y = [20, 25, 18, 15, 17, 20, 22]
    plt.plot(x[:4], y[:4], color="deepskyblue", label="actual")
    plt.plot(x[3:], y[3:], color="deepskyblue", linestyle="--", label="forecast")
    # plt.plot(x, y)
    plt.title("sales forecast")
    plt.ylabel("sales ('000)")
    plt.xlabel("year")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # demo()
    # demo2()
    # demo3()
    demo4()
