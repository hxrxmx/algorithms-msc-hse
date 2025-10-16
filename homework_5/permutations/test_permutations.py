from itertools import permutations as py_permutations

from homework_5.permutations.permutations import permutations


# run with flag: poetry run pytest -s homework_5/
# ("-s" flag enables printing from the tracer decorator)
def test_permutations():
    assert sorted(permutations([])) == [[]]

    assert sorted(permutations([1])) == sorted(
        [list(perm) for perm in py_permutations([1])]
    )

    assert sorted(permutations([1, 1, 2])) == sorted(
        [list(perm) for perm in py_permutations([1, 1, 2])]
    )

    assert sorted(permutations([0, 3, 3, 3, 8, 8])) == sorted(
        [list(perm) for perm in py_permutations([0, 3, 3, 3, 8, 8])]
    )
