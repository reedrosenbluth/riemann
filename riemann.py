from math import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def reimann(a, b, n, l, f):
    numRange = np.arange(a, b, .02)
    y = f(numRange)
    w = float(b - a)/n
    x = 0.0
    d = {"l": 0, "r": 1, "m": 0.5}
    offset = d[l[0]]
    for i in range(n):
        x += f(a + (i+offset)*w)
        plt.gca().add_patch(matplotlib.patches.Rectangle((i*w + a,0),w,f(a + (i+offset)*w)))
    plt.plot(numRange, y, color=(1.0, 0.00, 0.00), zorder=5)
    s = w * x
    print '\n', s, '\n'


def main():
    print #empty line
    functionString = raw_input("Enter a function: ")
    a = input("Enter the start point: ")
    b = input("Enter the end point: ")
    n = input("Enter the number of rectangles: ")
    l = raw_input("Type right, left, or middle: ")
    reimann(a, b, n, l, lambda x: eval(functionString))
    plt.show()

if __name__ == "__main__":
    main()
