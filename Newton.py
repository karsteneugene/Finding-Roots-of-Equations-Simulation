import numpy as np
from matplotlib import pyplot as plt


class Newton:

    # Takes in function, starting point x, figure, axis, and
    def __init__(self, f, x, fig, ax, h=1.0E-6):
        self.f = f
        self.x = x
        self.h = h
        self.fig = fig
        self.ax = ax

    def calculate(self):
        n = 0  # Set up a variable to count iterations

        # Lambda function to get the derivative of the function by using finite difference
        df = lambda: (self.f(self.x + self.h) - self.f(self.x - self.h)) / (2 * self.h)

        self.ax.set_title('Newton')  # Set the axis title as Newton

        # Loop while plotting until the result of the new x value inserted in the function is less than 1.0^-6
        # The loop contains pauses to be able to see the step-by-step process of the bisection
        while True:
            self.ax.plot(self.x, 0, 'ro')  # Plots a red point at (x, 0)
            plt.pause(0.5)
            self.ax.plot(self.x, self.f(self.x), 'o', c='midnightblue')  # Plots a blue point on (x, f(x))
            plt.pause(0.5)

            # Connect 2 previous plots with broken black line
            self.ax.plot([self.x, self.x], [0, self.f(self.x)], 'k--')
            plt.pause(0.5)

            temp = self.x  # Store the old x
            self.x = self.x - (self.f(self.x) / df())  # Get new x value by doing x - (f(x)/df(x))

            # Create broken line to the new x value from the previous point on graph
            self.ax.plot([temp, self.x], [self.f(temp), 0], '--', c='cornflowerblue')

            n += 1  # Add 1 to the number of iterations after every loop
            if n == 300:  # If iterations reach 100, stop the loop and return last x value and iterations
                return self.x, n
            if abs(self.f(self.x)) < 1.0E-6:                # If the absolute value of f(x) is less than 1.0x10^-6,
                self.ax.plot(self.x, 0, 'o', c='lime')      # Plots a bright green point at x to indicate it
                plt.pause(0.5)                              # found the closest approximation of the root
                return self.x, n                            # then return x and the number of iterations
