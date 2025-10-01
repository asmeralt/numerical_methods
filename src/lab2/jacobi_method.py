import numpy as np

from src.lab2.simple_iteration_base import *


def jacobi_method(
    A: SquareMatrix,
    b: ColumnVector,
    maxiter: int = 10,
    atol: float = 10**-7,
) -> ColumnVector:
    """Naive implementation of Jacobi method to solve system of linear equations.

    Args:
        A (SquareMatrix): A square matrix which represents left hand coeficients
        b (ColumnVector): A column vector of right hand side
        maxiter (int, optional): Maximum number of iterations. Defaults to 10.
        atol (float, optional): Desired absolute tolerance between two iterations. Defaults to 10**-7.

    Raises:
        ValueError: Raised when matrix is not two dimentional
        ValueError: Raised when matrix is not square (number of rows is not equal to number of columns)
        ValueError: Raised when matrix and column vector have different length
        ValueError: Raised when matrix A has not passed Jacobi convergence condition

    Returns:
        ColumnVector: Solution of SoLE
    """
    raise NotImplementedError("Jacobi method is not implemented yet")
