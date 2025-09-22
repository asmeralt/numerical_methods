import numpy as np
from src.lab1.gauss_method import gauss, swap_rows

import pytest

ATOL = 10**-7


def test_swap_rows_index_out_of_range():
    N = 2
    j = 3
    A = np.zeros((N, 2))
    with pytest.raises(IndexError) as e_info:
        swap_rows(A, 0, j)

    assert f"index {j} is out of bounds for axis 0 with size {N}" in str(e_info.value)


def test_swap_rows_neg_index():
    A = np.zeros((3, 3))
    A[0, :] = 1

    swap_rows(A, 0, -1)

    assert np.isclose(A.sum(axis=1), [0, 0, 3], atol=ATOL).all()


def test_swap_rows_1():
    A = np.zeros((3, 3))
    A[0, :] = 1

    swap_rows(A, 0, 1)

    assert np.isclose(A.sum(axis=1), [0, 3, 0], atol=ATOL).all()


def test_shape_2d():
    A = np.zeros((2, 2, 2))
    with pytest.raises(ValueError) as e_info:
        gauss(A, None)

    assert "Matrix A should have 2 dimensions" in str(e_info.value)


def test_shape_square():
    A = np.zeros((2, 3))
    with pytest.raises(ValueError) as e_info:
        gauss(A, None)

    assert "Matrix A should be square NxN" in str(e_info.value)


def test_shape_mismatch():
    A = np.zeros((2, 2))
    b = np.zeros(3)
    with pytest.raises(ValueError) as e_info:
        gauss(A, b)

    assert "Matrix A and vector b should be same length" in str(e_info.value)


def test_singular_matrix_1():
    A = np.asarray([[1, 2, 3], [1, 2, 3], [1, 2, -1]], dtype=np.float32)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    with pytest.raises(ValueError) as e_info:
        gauss(A, b)

    assert "Matrix A is singular" in str(e_info.value)


def generic_test(A, b):
    sol, detA, Ainv = gauss(A, b)

    assert (
        sol.shape == b.shape
    ), f"Solution shape {sol.shape} is wrong, should be {b.shape}"

    assert np.isfinite(detA), f"Determinant should be finite, but was {detA}"
    assert (
        Ainv.shape == A.shape
    ), f"Inverted matrix shape {Ainv.shape} is wrong, should be {A.shape}"

    sol_np = np.linalg.solve(A, b)
    detA_np = np.linalg.det(A)
    Ainv_np = np.linalg.inv(A)

    assert np.isclose(
        np.linalg.norm(sol - sol_np), 0.0, atol=ATOL
    ), f"Solution {sol} is wrong, should be {sol_np}"

    assert np.isclose(
        detA, detA_np, atol=ATOL
    ), f"Determinant {detA} is wrong, should be {detA_np} "

    assert np.isclose(
        np.linalg.norm((Ainv - Ainv_np).reshape(-1)), 0.0, atol=ATOL
    ), f"Inverted matrix {Ainv} is wrong, should be {Ainv_np} "


def test_1():
    A = np.asarray([[1, 2, 3], [-1, 0, 4], [1, 2, -1]], dtype=np.float32)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    generic_test(A, b)


def test_swap_rows():
    A = np.asarray([[1, 2, 3], [1, 2, 4], [1, 1, -1]], dtype=np.float32)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    generic_test(A, b)
