from numpy.random import randint

from homework_6.compare_n_iterative.timeit import timeit


@timeit
def quicksort_iterative(arr):
    return _quicksort_iterative(arr)


def _quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = randint(low, high + 1)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            pivot = arr[high]

            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]

            pivot_index = i + 1

            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

            if low < pivot_index - 1:
                stack.append((low, pivot_index - 1))

    return arr


@timeit
def quicksort_recursive(arr):
    return _quicksort_recursive(arr)


def _quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[randint(0, len(arr))]
    left_arr = []
    pivot_arr = []
    right_arr = []

    for elem in arr:
        if elem < pivot:
            left_arr.append(elem)
        elif elem > pivot:
            right_arr.append(elem)
        else:
            pivot_arr.append(elem)

    return _quicksort_recursive(left_arr) + pivot_arr + _quicksort_recursive(right_arr)


@timeit
def mergesort_iterative(arr):
    return _mergesort_iterative(arr)


def _mergesort_iterative(arr):
    sublists = [[x] for x in arr]

    while len(sublists) > 1:
        merged = []
        for i in range(0, len(sublists), 2):
            if i + 1 < len(sublists):
                merged.append(_merge(sublists[i], sublists[i + 1]))
            else:
                merged.append(sublists[i])
        sublists = merged

    return sublists[0] if sublists else []


@timeit
def mergesort_recursive(arr):
    return _mergesort_recursive(arr)


def _mergesort_recursive(arr):
    if len(arr) <= 1:
        return arr

    sep = len(arr) // 2
    left = _mergesort_recursive(arr[:sep])
    right = _mergesort_recursive(arr[sep:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
