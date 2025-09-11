from math import floor, sqrt


def count_primes(n):
    if n <= 2:
        return 0

    flags = [True] * n
    flags[0] = flags[1] = False

    for i in range(2, int(floor(sqrt(n)) + 1)):
        if not flags[i]:
            continue

        k = 2 * i
        while k < n:
            flags[k] = False
            k += i

    return sum(flags)
