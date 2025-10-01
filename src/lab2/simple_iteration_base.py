from typing import Annotated, Literal

import numpy as np
import numpy.typing as npt

SquareMatrix = Annotated[npt.NDArray[np.float32], Literal["N", "N"]]
ColumnVector = Annotated[npt.NDArray[np.float32], Literal["N"]]


def check_convergence_condition(A: SquareMatrix) -> bool:
    """Check simple condition
    if all the diagonal terms are greater than
    the sum of absolute values of other terms in corresponding row

    Args:
        A (SquareMatrix): A square matrix which represents left hand coeficients

    Returns:
        bool: an indicator whether Jacobi & Zeidel methods are applicable for this matrix A
    """
    raise NotImplementedError("Convergence condition check is not implemented yet")


def simple_iteration(
    xi: ColumnVector,
    M: SquareMatrix,
    N: SquareMatrix,
    b: ColumnVector,
    maxiter: int,
    atol: float,
):
    """A simple iteration method if form of x_next = M (b - N x_prev)

    Args:
        xi (ColumnVector): initial approximation
        N (SquareMatrix): A square matrix defined by a specific method
        M (SquareMatrix): A square matrix defined by a specific method
        b (ColumnVector): A column vector of right hand side
        maxiter (int): Maximum number of iterations
        atol (float): Desired absolute tolerance between two iterations

    Returns:
        ColumnVector: Approximation of SoLE solution
    """
    i = 0
    while i < maxiter:
        xj = np.dot(M, (b - np.dot(N, xi)))

        if np.linalg.norm(xi - xj) < atol:
            xi = xj
            break

        xi = xj
        i += 1

    return xi
