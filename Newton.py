import numpy as np
from matplotlib import pyplot as plt


class Newton:

    def __init__(self, f, x, fig, ax, h=1.0E-6):
        self.f = f
        self.x = x
        self.h = h
        self.fig = fig
        self.ax = ax

    def calculate(self):
        n = 0
        df = lambda: (self.f(self.x + self.h) - self.f(self.x - self.h)) / (2 * self.h)
        self.ax.set_title('Newton')
        while True:
            self.ax.plot(self.x, 0, 'ro')
            plt.pause(0.5)
            self.ax.plot(self.x, self.f(self.x), 'o', c='midnightblue')
            plt.pause(0.5)
            self.ax.plot([self.x, self.x], [0, self.f(self.x)], 'k--')
            plt.pause(0.5)
            temp = self.x
            self.x = self.x - (self.f(self.x) / df())
            self.ax.plot([temp, self.x], [self.f(temp), 0], '--', c='cornflowerblue')
            n += 1
            if n == 300:
                return self.x, n
            if abs(self.f(self.x)) < 1.0E-6:
                self.ax.plot(self.x, 0, 'o', c='lime')
                plt.pause(0.5)
                return self.x, n
