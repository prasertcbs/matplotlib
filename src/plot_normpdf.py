import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


def demo():
    mu, sigma = 0, 1
    x = np.linspace(-4, 4, 100)
    plt.plot(x, mlab.normpdf(x, mu, sigma))
    plt.show()


def demo2():
    mu = [0, 0, 0, 2]
    sigma = [.5, 1, 2, 1]
    linestyle = ["-", "--", "-.", ":"]
    x = np.linspace(-5, 5, 100)
    for m, s, ls in zip(mu, sigma, linestyle):
        plt.plot(x, mlab.normpdf(x, m, s),
                 label=r"$\mu={:.1f}, \sigma={:.1f}$".format(m, s),
                 linestyle=ls)
    plt.legend()
    plt.axvline(0, color=".8", linestyle="--")
    plt.axvline(2, color=".8", linestyle="--")
    plt.title("Probability Density Function")
    plt.show()


if __name__ == '__main__':
    # demo()
    demo2()
