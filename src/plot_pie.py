import matplotlib.pyplot as plt
import numpy as np

def demo():
    label = ("China", "Russia", "Japan", "Korea")
    val = (1.8, 1, .8, .5)
    plt.pie(val, labels=label, startangle=90, autopct = "%1.2f%%", explode=(0,0,0.1,0))
    plt.axis("equal")
    plt.show()

def demo2():
    label = np.array(["China", "Russia", "Japan", "Korea"])
    val = (1.8, 1, .8, .5)
    explode = np.zeros(label.size)
    # explode[2] = .1
    explode[np.where(label == "Korea")] = .1
    explode[np.where(label == "China")] = .1
    colors = ["red", "green", "pink", "orange"]
    # plt.pie(val, labels=label, startangle=90, autopct = "%1.2f%%", explode=explode)
    plt.pie(val, labels=label, startangle=90, autopct = "%1.2f%%", explode=explode, colors=colors)
    plt.axis("equal")
    plt.title("Tourists")
    plt.show()

if __name__ == '__main__':
    # demo()
    demo2()