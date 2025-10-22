from matplotlib.figure import Figure
import numpy as np
from src.lab3.utils import (
    parse_function,
    parse_derivative,
    parse_second_derivative,
    plot_equation,
)


def test_1():
    xstr = "x"
    fstr = "x^2-3*x+2"

    f = parse_function(xstr, fstr)

    assert f(0) == 2
    assert f(-1) == 6
    assert f(1) == 0


def test_2():
    xstr = "x"
    fstr = "x^2-3*x+2"

    df = parse_derivative(xstr, fstr)

    assert df(0) == -3
    assert df(-1) == -5
    assert df(1) == -1


def test_3():
    xstr = "x"
    fstr = "x^2-3*x+2"

    d2f = parse_second_derivative(xstr, fstr)

    assert d2f(0) == 2
    assert d2f(-1) == 2
    assert d2f(1) == 2


def test_4():
    xstr = "x"
    fstr = "x^2-3*x+2"

    x = np.linspace(-1, 1, 11)
    f = parse_function(xstr, fstr)
    df = parse_derivative(xstr, fstr)
    d2f = parse_second_derivative(xstr, fstr)

    fig = plot_equation(x, f, df, d2f)

    assert type(fig) == Figure
