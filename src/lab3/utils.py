from typing import Callable
from numpy import typing as npt

from matplotlib.figure import Figure


def parse_function(xstr: str, fstr: str) -> Callable:
    """Parses fstr into a function with xstr arguments

    Args:
        xstr (str): arguments
        fstr (str): function

    Returns:
        Callable: callable function
    """
    raise NotImplementedError("Method is not implemented yet")


def parse_derivative(xstr: str, fstr: str) -> Callable:
    """Parses fstr into a function with xstr arguments and differentiates

    Args:
        xstr (str): arguments
        fstr (str): function

    Returns:
        Callable: callable first derivative of function
    """
    raise NotImplementedError("Method is not implemented yet")


def parse_second_derivative(xstr: str, fstr: str) -> Callable:
    """Parses fstr into a function with xstr arguments and differentiates twice

    Args:
        xstr (str): arguments
        fstr (str): function

    Returns:
        Callable: callable second derivative of function
    """
    raise NotImplementedError("Method is not implemented yet")


def plot_equation(x: npt.NDArray, f: Callable, df: Callable, d2f: Callable) -> Figure:
    """Plots function f, its first and seconds derivatives values at points x

    Args:
        x (npt.NDArray): x-axis points
        f (Callable): function
        df (Callable): first derivative
        d2f (Callable): second derivative

    Returns:
        Figure: pyplot figure
    """
    raise NotImplementedError("Method is not implemented yet")
