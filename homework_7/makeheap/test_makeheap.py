import numpy as np
from pytest import fixture

from homework_7.makeheap.makeheap import makeheap, makeheap_n_log_n

SEED = 42
SIZE = 10_000_000

np.random.seed(SEED)


def is_minheap(arr):
    n = len(arr)
    for i in range(n // 2):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        if left_child_idx < n and arr[i] > arr[left_child_idx]:
            return False

        if right_child_idx < n and arr[i] > arr[right_child_idx]:
            return False

    return True


@fixture
def test_cases():
    return [
        [],
        [5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 1, 3, 2, 16, 9, 10, 14, 8, 7],
        [5, 8, 2, 5, 2],
        [float(x) for x in np.random.randint(-SIZE, SIZE, SIZE)],
    ]


def test_makeheap_n_log_n(test_cases):
    print(f"------- makeheap: O(n log n), last heap size = {SIZE}--------")
    for case_arr in test_cases:
        arr_copy = list(case_arr)
        makeheap_n_log_n(arr_copy)
        assert is_minheap(arr_copy)


def test_makeheap_O_N(test_cases):
    print(f"------- makeheap: O(n), last heap size = {SIZE}--------")
    for case_arr in test_cases:
        arr_copy = list(case_arr)
        makeheap(arr_copy)
        assert is_minheap(arr_copy)
