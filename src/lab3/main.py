from matplotlib import pyplot as plt
import numpy as np
from src.lab3.utils import (
    parse_function,
    parse_derivative,
    parse_second_derivative,
    plot_equation,
)
from src.lab3.chord_method import (
    choose_initial_approximation as choose_chord,
    chord_method,
)
from src.lab3.tangent_method import (
    choose_initial_approximation as choose_tangent,
    tangent_method,
)


if __name__ == "__main__":
    xstr = "x"
    fstr = "-sin(x**2)-3*x+1"

    x = np.linspace(-1, 2, 101)
    f = parse_function(xstr, fstr)
    df = parse_derivative(xstr, fstr)
    d2f = parse_second_derivative(xstr, fstr)
    fig = plot_equation(x, f, df, d2f)
    plt.show()

    a, b = 0.25, 0.5

    print("Chord method")
    x0, x1 = choose_chord(a, b, fstr)
    print(x0, x1)
    sol = chord_method(x0, x1, fstr)
    print(sol)
    print("-" * 30)

    print("Tangent method")
    x0 = choose_tangent(a, b, fstr)
    print(x0)
    sol = tangent_method(x0, fstr)
    print(sol)
    print("-" * 30)
