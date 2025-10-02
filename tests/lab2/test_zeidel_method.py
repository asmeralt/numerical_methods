import numpy as np
import pytest

from src.lab2.zeidel_method import zeidel_method

ATOL = 10**-2


def test_shape_2d():
    A = np.zeros((2, 2, 2))
    with pytest.raises(ValueError) as e_info:
        zeidel_method(A, None)

    assert "Matrix A should have 2 dimensions" in str(e_info.value)


def test_shape_square():
    A = np.zeros((2, 3))
    with pytest.raises(ValueError) as e_info:
        zeidel_method(A, None)

    assert "Matrix A should be square NxN" in str(e_info.value)


def test_shape_mismatch():
    A = np.zeros((2, 2))
    b = np.zeros(3)
    with pytest.raises(ValueError) as e_info:
        zeidel_method(A, b)

    assert "Matrix A and vector b should be same length" in str(e_info.value)


def test_singular_matrix_1():
    A = np.ones((3, 3), dtype=np.float32)
    b = np.zeros(3)

    with pytest.raises(ValueError) as e_info:
        zeidel_method(A, b)

    assert "Matrix A has not passed Jacobi convergence condition." in str(e_info.value)


def test_1():
    A = np.asarray([[6, 2, 3], [-1, -5, 4], [1, 2, -5]], dtype=np.float32)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    sol = zeidel_method(A, b)
    sol_np = np.linalg.solve(A, b)

    assert np.isclose(np.linalg.norm(sol - sol_np), 0.0, atol=ATOL)


def test_1_maxerror():
    A = np.asarray([[5, 2, 3], [-1, -5, 4], [1, 2, -3]], dtype=np.float32)
    A = np.divide(A, 10000)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    sol = zeidel_method(A, b)
    sol_np = np.linalg.solve(A, b)

    assert np.linalg.norm(sol - sol_np) < 0.457
