import matplotlib.pyplot as plt
import numpy as np


def demo_dual_y():
    labels = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
    x = np.arange(labels.size)
    y1 = np.random.normal(800, 90, labels.size)
    fig, ax1 = plt.subplots()
    ax1.bar(x, y1, color="purple", alpha=.3)
    ax1.set_ylabel("sales ('000)", color="purple", fontsize=12)
    ax1.tick_params("y", colors="purple")

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.legend()
    ax1.set_title("Sales vs. Profit (Jan-Jun 2017)")

    ax2 = ax1.twinx()
    y2 = np.random.normal(80, 10, labels.size)
    ax2.plot(x, y2, marker="o", color="green")
    ax2.tick_params("y", colors="green")
    ax2.set_ylabel("profit", color="green", fontsize=12)
    ax2.set_ylim(ymin=0)

    plt.show()


if __name__ == '__main__':
    demo_dual_y()
