import numpy as np

from src.lab2.jacobi_method import jacobi_method
from src.lab2.simple_iteration_base import check_convergence_condition, simple_iteration
from src.lab2.zeidel_method import zeidel_method

if __name__ == "__main__":
    A = np.asarray([[6, 2, 3], [-1, -5, 4], [1, 2, -5]], dtype=np.float32)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    sol = np.linalg.solve(A, b)
    print(*sol.round(2))

    print("Simple iteration method appliance", check_convergence_condition(A))
    sol_jacobi = jacobi_method(A, b)
    print(f"Jacobi {np.linalg.norm(sol - sol_jacobi):.2f}", *sol_jacobi.round(2))

    sol_zeidel = zeidel_method(A, b)
    print(f"Zeidel {np.linalg.norm(sol - sol_zeidel):.2f} ", *sol_zeidel.round(2))

    ATOL = 10**-7
    xi = np.ones(3, dtype=np.float32)
    M = np.eye(3, dtype=np.float32)
    N = np.eye(3, dtype=np.float32)
    b = 2 * np.ones(3, dtype=np.float32)

    xj = simple_iteration(xi, M, N, b, maxiter=1, atol=ATOL)

    print(xj)
