from homework_1.palindrome.is_palindrome import is_palindrome


def test_palindrome_numbers():
    assert is_palindrome(0)
    assert is_palindrome(11)
    assert is_palindrome(121)
    assert is_palindrome(int("134614356226134" + "134614356226134"[::-1]))


def test_non_palindrome_numbers():
    assert not is_palindrome(10)
    assert not is_palindrome(123)
    assert not is_palindrome(int("134614356226134" + "34614356226134"[::-1]))
