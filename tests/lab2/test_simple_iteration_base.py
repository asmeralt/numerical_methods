import numpy as np
import pytest

from src.lab2.simple_iteration_base import check_convergence_condition, simple_iteration

ATOL = 10**-7


def test_check_convergence_condition_true():
    A = np.asarray([[10, 1, 1], [1, -10, 1], [1, 9, 10]], dtype=np.float32)

    assert check_convergence_condition(A)


def test_check_convergence_condition_false():
    A = np.asarray([[10, 1, 1], [1, -10, 1], [1, 9.1, 10]], dtype=np.float32)

    assert not check_convergence_condition(A)


def test_simple_iteration():
    xi = np.ones(3, dtype=np.float32)
    M = np.eye(3, dtype=np.float32)
    N = np.eye(3, dtype=np.float32)
    b = 2 * np.ones(3, dtype=np.float32)

    xj = simple_iteration(xi, M, N, b, maxiter=1, atol=ATOL)

    assert np.isclose(np.linalg.norm(xi - xj), 0, atol=ATOL)
