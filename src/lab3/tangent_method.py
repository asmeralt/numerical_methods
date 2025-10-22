def choose_initial_approximation(
    a: float,
    b: float,
    fstr: str,
) -> float:
    """Chooses initial approximation for Tangent method to find root of the 'f(x) = 0' equation in range [a, b].
    Initial approximation in this case in either left (a) or right (b) end of the interval.

    Args:
        a (float): left interval border
        b (float): right interval border
        fstr (str): function str which represents left side of the 'f(x) = 0' equation

    Raises:
        ValueError: raises when sufficient condition is false for both ends

    Returns:
        float: initial approximation which is either a or b
    """
    raise NotImplementedError("Method is not implemented yet")


def tangent_method(
    x0: float,
    fstr: str,
    maxiter: int = 10,
    atol: float = 10**-7,
) -> float:
    """Naive implementation of Tangent (Newton) method for numerical solving of 'f(x) = 0' equation.
    Uses 'x0' as initial approximation of the root.

    Args:
        x0 (float): initial approximation of the root.
        fstr (str): function str which represents left side of the 'f(x) = 0' equation.
        maxiter (int, optional): Maximum number of iterations. Defaults to 10.
        atol (float, optional): Desired absolute tolerance between two iterations. Defaults to 10**-7.

    Returns:
        float: the root of 'f(x) = 0'
    """
    raise NotImplementedError("Tangent method is not implemented yet")
