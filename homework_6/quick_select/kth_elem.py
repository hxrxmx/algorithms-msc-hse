from numpy.random import randint


def k_th(arr, k):
    pivot = arr[randint(0, len(arr))]

    left = []
    pivots = []
    right = []

    for elem in arr:
        if elem > pivot:
            right.append(elem)
        elif elem < pivot:
            left.append(elem)
        else:
            pivots.append(elem)

    if len(left) > k:
        return k_th(left, k)
    elif len(left) + len(pivots) > k:
        return pivot
    else:
        return k_th(right, k - len(left) - len(pivots))
