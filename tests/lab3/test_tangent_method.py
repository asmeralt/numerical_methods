from src.lab3.utils import parse_function
from src.lab3.tangent_method import (
    choose_initial_approximation as choose_chord,
    tangent_method,
)
import numpy as np

ATOL = 10**-7


def test_1():
    xstr = "x"
    fstr = "sin(x**2)-3*x+1"
    f = parse_function(xstr, fstr)
    a, b = 0.25, 0.5

    x0 = choose_chord(a, b, fstr)

    assert np.isclose(x0, a, atol=ATOL)

    sol = tangent_method(x0, fstr)

    assert np.isclose(f(sol), 0.0, atol=ATOL)


def test_2():
    xstr = "x"
    fstr = "-sin(x**2)-3*x+1"
    f = parse_function(xstr, fstr)
    a, b = 0.25, 0.5

    x0 = choose_chord(a, b, fstr)

    assert np.isclose(x0, b, atol=ATOL)

    sol = tangent_method(x0, fstr)

    assert np.isclose(f(sol), 0.0, atol=ATOL)


def test_3():
    xstr = "x"
    fstr = "x^2-3*x+2"
    f = parse_function(xstr, fstr)
    a, b = 0.5, 1.5

    x0 = choose_chord(a, b, fstr)

    assert np.isclose(x0, a, atol=ATOL)

    sol = tangent_method(x0, fstr)

    assert np.isclose(f(sol), 0.0, atol=ATOL)


def test_4():
    xstr = "x"
    fstr = "-x^2-3*x+2"
    f = parse_function(xstr, fstr)
    a, b = 0.5, 1.5

    x0 = choose_chord(a, b, fstr)

    assert np.isclose(x0, b, atol=ATOL)

    sol = tangent_method(x0, fstr)

    assert np.isclose(f(sol), 0.0, atol=ATOL)
