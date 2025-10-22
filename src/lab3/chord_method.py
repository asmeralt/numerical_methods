from typing import Tuple


def choose_initial_approximation(
    a: float,
    b: float,
    fstr: str,
) -> Tuple[float, float]:
    """Chooses initial approximation for Chord method to find root of the 'f(x) = 0' equation in range [a, b].
    Initial approximation in this case is a pair of x0 (starting point of all chords) and x1 (ending point for initial chord).
    Returned

    Args:
        a (float): left interval border
        b (float): right interval border
        fstr (str): function str which represents left side of the 'f(x) = 0' equation

    Raises:
        ValueError: raises when sufficient condition is false for both ends

    Returns:
        Tuple[float, float]: initial approximation, either tuple of (a, b) or (b, a)
    """
    raise NotImplementedError("Method is not implemented yet")


def chord_method(
    x0: float,
    x1: float,
    fstr: str,
    maxiter: int = 10,
    atol: float = 10**-7,
) -> float:
    """Naive implementation of Chord method for numerical solving of 'f(x) = 0' equation.
    Uses x0 as starting point for all chords and x1 as ending point of initial chord.

    Args:
        x0 (float): starting point of all chords
        x1 (float): ending point of initial chord
        fstr (str): function str which represents left side of the 'f(x) = 0' equation.
        maxiter (int, optional): Maximum number of iterations. Defaults to 10.
        atol (float, optional): Desired absolute tolerance between two iterations. Defaults to 10**-7.

    Returns:
        float: the root of 'f(x) = 0'
    """
    raise NotImplementedError("Chord method is not implemented yet")
