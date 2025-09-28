from homework_3.two_sum.sum_ids_search import sum_ids


def test_two_sum():
    assert sum_ids([1, 3, 4, 120], 7) == (1, 2)
    assert sum_ids([1, -3, 100, 3, -101], 0) == (1, 3)
    assert sum_ids([0, 2, 0], 0) == (0, 2)
    assert sum_ids([i for i in range(1_000_000)], 1_000_000) == (499999, 500001)
