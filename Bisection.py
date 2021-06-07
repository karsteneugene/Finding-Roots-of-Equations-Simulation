import numpy as np
from matplotlib import pyplot as plt


class Bisection:
    def __init__(self, f, xl, xr, fig, ax):
        self.f = f
        self.xl = xl
        self.xr = xr
        self.fig = fig
        self.ax = ax

    def calculate(self):
        if self.f(self.xl) * self.f(self.xr) > 0:
            print("Root are not found between points")
        else:
            n = 0
            self.ax.set_title('Bisection')
            while True:
                self.ax.plot(self.xl, 0, 'o', c='midnightblue')
                plt.pause(0.5)
                plt.axvline(self.xl, c='cornflowerblue', ls='--')
                plt.pause(0.5)
                self.ax.plot(self.xr, 0, 'o', c='midnightblue')
                plt.pause(0.5)
                plt.axvline(self.xr, c='cornflowerblue', ls='--')
                plt.pause(0.5)
                xm = (self.xl + self.xr) / 2
                self.ax.plot(xm, 0, 'o', c='lime')
                plt.pause(0.5)
                plt.pause(0.5)
                if self.f(self.xl) * self.f(xm) < 0:
                    self.xr = xm
                else:
                    self.xl = xm
                n += 1
                if n == 100:
                    return xm, n
                if abs(self.f(xm)) < 1.0E-6:
                    return xm, n
