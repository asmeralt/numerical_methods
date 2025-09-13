import numpy as np
from src.examples.example2 import create_eye_square_matrix


def test():
    N = 10
    M = create_eye_square_matrix(N)

    assert np.trace(M) == N
