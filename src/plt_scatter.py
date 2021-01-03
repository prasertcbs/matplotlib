import matplotlib.pyplot as plt
from scipy import stats


def demo():
    x = [170, 165, 180, 155, 163, 160, 175]
    y = [80, 65, 75, 47, 50, 52, 74]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print(slope, intercept, r_value ** 2, p_value)
    l = slope * min(x) + intercept, slope * max(x) + intercept
    plt.scatter(x, y)
    plt.plot([min(x), max(x)], l, linestyle="--", alpha=.5, color="green")
    plt.xlabel("height (cm.)")
    plt.ylabel("weight (kg.)")
    # t = "y = {:.2f} + {:.2f}x, r^2 = {:.4f}, p = {:.4}".format(intercept, slope, r_value ** 2, p_value)
    t = r"${} = {:.2f} + {:.2f}x, r^2 = {:.4f}, p = {:.4}$".format("\^{y}", intercept,
                                                                   slope, r_value ** 2,
                                                                   p_value)
    plt.title(t)
    plt.show()


if __name__ == '__main__':
    demo()
