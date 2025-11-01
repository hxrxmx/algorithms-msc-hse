import numpy as np
from pytest import fixture

from homework_6.compare_n_iterative.sort import (
    mergesort_iterative,
    mergesort_recursive,
    quicksort_iterative,
    quicksort_recursive,
)

# run with flag: poetry run pytest -s homework_6/
# ("-s" flag enables printing from the timeit decorator)

SEED = 42
SIZE = 10_000

np.random.seed(SEED)


@fixture
def random_array():
    return np.random.randint(0, SIZE, SIZE).tolist()


@fixture
def sorted_array():
    return [i for i in range(SIZE)]


@fixture
def reverse_sorted_array():
    return [i for i in range(SIZE)][::-1]


@fixture
def identical_arr():
    return [0] * SIZE


def test_sort_simple():
    print("------- Simple Arrays --------")

    assert mergesort_iterative([]) == []
    assert mergesort_recursive([]) == []
    assert quicksort_iterative([]) == []
    assert quicksort_recursive([]) == []

    assert mergesort_iterative([1]) == [1]
    assert mergesort_recursive([1]) == [1]
    assert quicksort_iterative([1]) == [1]
    assert quicksort_recursive([1]) == [1]

    assert mergesort_iterative([1, 1]) == [1, 1]
    assert mergesort_recursive([1, 1]) == [1, 1]
    assert quicksort_iterative([1, 1]) == [1, 1]
    assert quicksort_recursive([1, 1]) == [1, 1]

    assert mergesort_iterative([1, 0]) == [0, 1]
    assert mergesort_recursive([1, 0]) == [0, 1]
    assert quicksort_iterative([1, 0]) == [0, 1]
    assert quicksort_recursive([1, 0]) == [0, 1]


def test_sort_random_time(random_array):
    print("------- Random Array --------")

    expected = sorted(random_array)
    assert mergesort_recursive(random_array.copy()) == expected
    assert quicksort_recursive(random_array.copy()) == expected
    assert mergesort_iterative(random_array.copy()) == expected
    assert quicksort_iterative(random_array.copy()) == expected


def test_sort_identical_time(identical_arr):
    print("------- Identical Array --------")

    expected = identical_arr
    assert mergesort_recursive(identical_arr.copy()) == expected
    assert quicksort_recursive(identical_arr.copy()) == expected
    assert mergesort_iterative(identical_arr.copy()) == expected
    assert quicksort_iterative(identical_arr.copy()) == expected


def test_sort_sorted_time(sorted_array):
    print("------- Sorted Array --------")

    expected = sorted_array
    assert mergesort_recursive(sorted_array.copy()) == expected
    assert quicksort_recursive(sorted_array.copy()) == expected
    assert mergesort_iterative(sorted_array.copy()) == expected
    assert quicksort_iterative(sorted_array.copy()) == expected


def test_sort_reversed_time(reverse_sorted_array):
    print("------- Reversed Sorted Array --------")

    expected = reverse_sorted_array[::-1]
    assert mergesort_recursive(reverse_sorted_array.copy()) == expected
    assert quicksort_recursive(reverse_sorted_array.copy()) == expected
    assert mergesort_iterative(reverse_sorted_array.copy()) == expected
    assert quicksort_iterative(reverse_sorted_array.copy()) == expected
