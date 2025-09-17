from typing import Annotated, Literal, Tuple

import numpy as np
import numpy.typing as npt

SquareMatrix = Annotated[npt.NDArray[np.float32], Literal["N", "N"]]
ColumnVector = Annotated[npt.NDArray[np.float32], Literal["N"]]


def swap_rows(M: npt.NDArray, i: int, j: int) -> None:
    """Swap i-th and j-th rows in two dimentional array

    Args:
        M (npt.NDArray): A rectangular two dimentional NDArray
        i (int): an index of i-th row
        j (int): an index of j-th row
    """
    raise NotImplementedError("This Rows Swap is not implemented yet")


def gauss(
    A: SquareMatrix,
    b: ColumnVector,
    atol: float = 10**-7,
) -> Tuple[ColumnVector, float, SquareMatrix]:
    """Naive implementation of Gauss solver for system of linear equations.
    This code not only solves SoLE but also returns determinant of matrix A and inverted matrix A^-1

    Args:
        A (SquareMatrix): A square matrix which represents left hand coeficients
        b (ColumnVector): A column vector of right hand side
        atol (float): Absolute tolerance to check matrix for singularity

    Raises:
        ValueError: Raised when matrix is not two dimentional
        ValueError: Raised when matrix is not square (number of rows is not equal to number of columns)
        ValueError: Raised when matrix and column vector have different length
        ValueError: Raised when matrix is singular

    Returns:
        Tuple[ColumnVector, float, SquareMatrix]: Solution of SoLE, determinant of A, inverted A^-1
    """
    raise NotImplementedError("This Gauss Method is not implemented yet")
