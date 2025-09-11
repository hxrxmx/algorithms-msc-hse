from homework_1.sum.max_even_sum import max_even_sum


def test_max_even_sum():
    assert max_even_sum([]) == 0
    assert max_even_sum([0]) == 0
    assert max_even_sum([2]) == 2
    assert max_even_sum([3]) == 0
    assert max_even_sum([2, 4, 6]) == 12
    assert max_even_sum([1, 3, 5]) == 8
    assert max_even_sum([3, 4, 5, 4, 6, 3]) == 22
    assert max_even_sum([3, 4, 5, 4, 6, 3, 5]) == 30
