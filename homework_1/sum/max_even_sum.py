from math import inf


def max_even_sum(arr):
    full_sum = sum(arr)

    if full_sum % 2 == 0:
        return full_sum
    else:
        min_odd_elem = inf
        for elem in arr:
            if elem % 2 != 0 and elem < min_odd_elem:
                min_odd_elem = elem
        return full_sum - min_odd_elem
