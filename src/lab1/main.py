import numpy as np

from src.lab1.gauss_method import gauss


def main():
    A = np.asarray([[1, 2, 3], [-1, 0, 4], [1, 2, -1]], dtype=np.float32)
    A = np.asarray([[1, 2, 3], [1, 2, 4], [1, 1, -1]], dtype=np.float32)
    b = np.asarray([1, 1, 1], dtype=np.float32)

    print(*gauss(A, b), sep="\n")
    print(30 * "-")

    x = np.linalg.solve(A, b)
    print(x)
    print(30 * "-")

    detA = np.linalg.det(A)
    print(detA)
    print(30 * "-")
    Ainv = np.linalg.inv(A)
    print(Ainv)


if __name__ == "__main__":
    main()
