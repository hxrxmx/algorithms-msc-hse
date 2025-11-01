import numpy as np

from homework_6.quick_select.kth_elem import k_th

SEED = 42

np.random.seed(SEED)


def test_k_th():
    arr = [3, 1, 4, 1, 5, 9, 2]
    assert k_th(arr.copy(), 0) == 1
    assert k_th(arr.copy(), 3) == 3
    assert k_th(arr.copy(), 6) == 9

    arr = [1, 2, 3, 4, 5]
    for k in range(len(arr)):
        assert k_th(arr.copy(), k) == arr[k]

    arr = [7] * 10
    for k in range(len(arr)):
        assert k_th(arr.copy(), k) == 7

    arr = [5, 4, 3, 2, 1]
    assert k_th(arr.copy(), 0) == 1
    assert k_th(arr.copy(), 2) == 3
    assert k_th(arr.copy(), 4) == 5
