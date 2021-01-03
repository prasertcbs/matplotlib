import matplotlib.pyplot as plt
import numpy as np


def demo():
    labels = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
    x = np.arange(labels.size)
    y1 = np.random.normal(80, 10, x.size)
    y2 = np.random.normal(95, 12, x.size)
    plt.bar(x, y1, color="deepskyblue", alpha=.3, label="we")
    plt.plot(x, y2, color="orange", label="industry", marker="o")
    plt.xticks(x, labels)
    plt.legend()
    plt.title("Sales (Jan-Jun 2017)")
    plt.ylabel("Sales ('000)")
    plt.show()


if __name__ == '__main__':
    demo()
