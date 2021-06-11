import numpy as np
from matplotlib import pyplot as plt


class Bisection:

    # Takes in the function, lower bound, upper bound, figure and axis
    def __init__(self, f, xl, xr, fig, ax):
        self.f = f
        self.xl = xl
        self.xr = xr
        self.fig = fig
        self.ax = ax

    def calculate(self):
        # Checks to see if a root is found by putting the lower bound and upper bound in the function and multiply
        # them together
        if self.f(self.xl) * self.f(self.xr) > 0:  # If it is more than 0, there are no roots
            print("Root are not found between points")
        else:
            n = 0  # Set up a variable to count iterations
            self.ax.set_title('Bisection')  # Set the axis title as Bisection

            # Loop while plotting until the result of the mid point inserted in the function is less than 1.0^-6
            # The loop contains pauses to be able to see the step-by-step process of the bisection
            while True:
                self.ax.plot(self.xl, 0, 'o', c='midnightblue')  # Plots a blue point on the lower bound
                plt.pause(0.5)
                plt.axvline(self.xl, c='cornflowerblue', ls='--')  # Plots a broken straight line up on the lower bound
                plt.pause(0.5)
                self.ax.plot(self.xr, 0, 'o', c='midnightblue')  # Plots a blue point on the upper bound
                plt.pause(0.5)
                plt.axvline(self.xr, c='cornflowerblue', ls='--')  # Plots a broken straight line up on the upper bound
                plt.pause(0.5)

                # Get the middle point by adding upper and lower and divide the result by 2
                xm = (self.xl + self.xr) / 2

                self.ax.plot(xm, 0, 'o', c='lime')  # Plots a bright green point on the mid point
                plt.pause(0.5)
                plt.pause(0.5)

                # Checks the value when f(xl) is multiplied with f(xm)
                if self.f(self.xl) * self.f(xm) < 0:
                    self.xr = xm  # If it's less than 0, the midpoint becomes the new upper bound
                else:
                    self.xl = xm  # If it's more than 0, the midpoint becomes the new lower bound
                n += 1  # Add 1 to the number of iterations after every loop
                if n == 100:  # If iterations reach 100, stop the loop and return last midpoint and iterations
                    return xm, n
                if abs(self.f(xm)) < 1.0E-6:    # If the absolute value of f(xm) is less than 1.0x10^-6,
                    return xm, n                # it has found the closest approximate of the root and returns that
                                                # with the number of iterations
