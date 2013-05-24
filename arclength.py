from math import *
import parser

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

DEBUG = False

def arclength(a, b, n, f):
    numRange = np.arange(a, b, .02)
    y = f(numRange)
    w = float(b - a)/n
    x = a
    dist = 0
    while x < b:
        x1, x2 = x, x+w
        y1, y2 = f(x1), f(x2)
        plt.plot([x1,x2], [y1,y2], color=(0.00, 0.00, 1.00))
        dist += sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
        x += w
    plt.plot(numRange, y, color=(1.00, 0.00, 0.00), zorder=5)
    print "\n", dist , "\n"

def main():
    if DEBUG:
        arclength(0, 10, 5, lambda x: x**2)
        plt.show()
    else:
        functionString = raw_input("\nEnter a function: ")
        code = parser.expr(functionString).compile()
        a = input("Enter the start point: ")
        b = input("Enter the end point: ")
        n = input("Enter the number of lines: ")
        arclength(a, b, n, lambda x: eval(code))
        plt.show()

if __name__=="__main__":
    main()
