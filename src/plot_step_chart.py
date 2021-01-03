import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

def fmt_pct(val, pos):
    return "{:.1f}%".format(100 * val)

def demo():
    labels = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
    x = np.arange(labels.size)
    y = np.random.randint(1, 8, x.size) / 100
    fig, ax = plt.subplots(1, 3, sharey=True)
    ax[0].yaxis.set_major_formatter(FuncFormatter(fmt_pct))

    plt.sca(ax[0])
    plt.plot(x, y, marker="o")
    plt.xticks(x, labels)
    plt.title("Line")

    plt.sca(ax[1])
    plt.step(x, y, marker="o", color="orange", where="pre")
    plt.xticks(x, labels)
    plt.title("Step (pre)")

    plt.sca(ax[2])
    plt.step(x, y, marker="o", color="green", where="post")
    plt.xticks(x, labels)
    plt.title("Step (post)")
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    demo()