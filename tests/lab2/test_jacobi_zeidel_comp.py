import numpy as np
import pytest

from src.lab2.jacobi_method import jacobi_method
from src.lab2.zeidel_method import zeidel_method

ATOL = 10**-2


def test_1():
    A = np.asarray([[5, 2, 3], [-1, -5, 4], [1, 2, -3]], dtype=np.float32)
    A = np.divide(A, 10000)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    sol_np = np.linalg.solve(A, b)

    sol_jacobi = jacobi_method(A, b)
    err_jacobi = np.linalg.norm(sol_np - sol_jacobi)

    sol_zeidel = zeidel_method(A, b)
    err_zeidel = np.linalg.norm(sol_np - sol_zeidel)

    assert err_jacobi >= err_zeidel
