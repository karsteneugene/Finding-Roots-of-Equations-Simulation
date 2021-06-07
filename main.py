from Newton import Newton
from Bisection import Bisection
import numpy as np
from matplotlib import pyplot as plt


def main():
    # Print statements to show the Main Menu with all its instructions
    print("****** MAIN MENU ******")
    print("\nInstructions:")
    print("1. For trigonometric identities (sin, cos, tan), exponents, and logarithms, use 'np.' in front of them")
    print("Example: np.sin, np.cos, np.tan, np.exp, np.log\n")
    print(
        "2. For multiplication, use the asterisk (*) symbol. For division, use the slash (/) symbol. For power (x^2), "
        "use double asterisk (**) symbol")
    print("Example: 2*x, x/4, x**3\n")
    print("3. Use 'x' as the variable for the equation.")
    print("Example: 2*x + 1, 4*x**2 - 2*x + 1\n")

    # Catching an exception when the user uses the wrong syntax or name
    while True:
        try:
            user_f = input("Enter your function: ")
            f = eval("lambda x:" + user_f)
            f(0)    # Checks if the function is valid by inserting 0 inside it
        except NameError:
            print("\nInvalid input! Please re-read the instructions.")
            continue
        except SyntaxError:
            print("\nInvalid input! Please re-read the instructions.")
            continue
        else:
            break

    x_lin = np.linspace(-20, 20, 1000)

    # Setting up the figure and graph
    plt.style.use('ggplot')
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_lin, f(x_lin))
    ax.set_xlabel('x-axis')
    ax.set_ylabel('f(x)')

    # Catching an exception for when the user inputs anything other than an integer
    while True:
        while True:
            try:
                print("\nChoose your method of solution:")
                print("1. Bisection")
                print("2. Newton")
                user_input = int(input("\n>> "))
            except ValueError:
                print("\nInvalid input! Please only enter 1 or 2.")
            else:
                break

        # If user input is 1, asks for lower and upper bound, also catches and exception if bounds are not valid,
        # then initiates the bisection method
        if user_input == 1:
            while True:
                try:
                    print("\nEnter the lower and upper bound:")
                    user_xl = float(input("Lower bound: "))
                    user_xr = float(input("Upper bound: "))
                    bisection = Bisection(f, user_xl, user_xr, fig, ax)
                    root_bisection, iterations_bisection = bisection.calculate()
                except TypeError:
                    print("\nInvalid bounds, please try again")
                    continue
                else:
                    return root_bisection, iterations_bisection

        # If user input is 2, asks for the starting point x and initiate Newton Raphson's method
        elif user_input == 2:
            user_x = float(input("\nEnter the starting point: "))
            newton = Newton(f, user_x, fig, ax)
            root_newton, iterations_newton = newton.calculate()
            return root_newton, iterations_newton

        # If user inputs integers besides 1 or 2, asks them to retry
        else:
            print("\nInvalid input! Please only enter 1 or 2.")
            continue


if __name__ == "__main__":
    root, iterations = main()
    print(f'Root: {root}, Iterations: {iterations}')
    plt.show()
