from homework_2.validate.validate import validate_stack_sequences


def test_validate_stack_sequences():
    assert validate_stack_sequences([1, 2, 3, 4, 5], [1, 3, 5, 4, 2])
    assert not validate_stack_sequences([1, 2, 3], [3, 1, 2])

    assert validate_stack_sequences([1], [1])
    assert validate_stack_sequences([1, 2], [2, 1])
    assert validate_stack_sequences([1, 2], [1, 2])

    n = 1000
    pushed = list(range(1, n + 1))
    popped = pushed[::-1]
    assert validate_stack_sequences(pushed, popped)
