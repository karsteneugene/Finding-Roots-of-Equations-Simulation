from Newton import Newton
from Bisection import Bisection
import numpy as np
from matplotlib import pyplot as plt


def main():
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

    while True:
        try:
            user_f = input("Enter your function: ")
            f = eval("lambda x:" + user_f)
            f(0)
        except NameError:
            print("\nInvalid input! Please re-read the instructions.")
            continue
        except SyntaxError:
            print("\nInvalid input! Please re-read the instructions.")
            continue
        else:
            break

    x_lin = np.linspace(-20, 20, 1000)

    plt.style.use('ggplot')
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_lin, f(x_lin))
    ax.set_xlabel('x-axis')
    ax.set_ylabel('f(x)')

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

        elif user_input == 2:
            user_x = float(input("\nEnter the starting point: "))
            newton = Newton(f, user_x, fig, ax)
            root_newton, iterations_newton = newton.calculate()
            return root_newton, iterations_newton

        else:
            print("\nInvalid input! Please only enter 1 or 2.")
            continue


if __name__ == "__main__":
    root, iterations = main()
    print(f'Root: {root}, Iterations: {iterations}')
    plt.show()
