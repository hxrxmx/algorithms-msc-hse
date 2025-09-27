from homework_2.merge_lists.merge_lists import merge


def test_merge():
    assert merge([1, 1, 2, 4], [1, 2, 3]) == [1, 1, 1, 2, 2, 3, 4]

    assert merge([i for i in range(100)], [i for i in range(100)]) == [
        i // 2 for i in range(200)
    ]
