import numpy as np
import numpy.typing as npt


def create_eye_square_matrix(N: int, dtype: npt.DTypeLike = np.int32) -> npt.NDArray:
    return np.eye(N, dtype=dtype)
