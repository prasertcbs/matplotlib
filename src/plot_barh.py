import matplotlib.pyplot as plt

def barv():
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("mocha", "latte", "espresso", "tea")
    plt.xticks(x, xticks)
    plt.bar(x, y)
    plt.show()

def barh():
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("mocha", "latte", "espresso", "tea")
    plt.yticks(x, xticks)
    plt.barh(x, y)
    plt.show()

def bar_subplot():
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("mocha", "latte", "espresso", "tea")
    fig, ax = plt.subplots(2, 1)
    ax[0].bar(x, y, color = "green")
    ax[1].barh(x, y, color = "purple")
    plt.sca(ax[0])
    plt.xticks(x, xticks)
    plt.sca(ax[1])
    plt.yticks(x, xticks)
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    # barv()
    # barh()
    bar_subplot()