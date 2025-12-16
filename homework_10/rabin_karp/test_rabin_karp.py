from homework_10.rabin_karp.rabin_karp import rabin_karp_search


def test_basic_match():
    assert rabin_karp_search("huuuuuuh", "uh") == 6


def test_match_at_start():
    assert rabin_karp_search("algorithm", "algo") == 0


def test_no_match():
    assert rabin_karp_search("abcdefg", "xyz") == -1


def test_long_pattern():
    assert rabin_karp_search("short text", "looooooooong pattern") == -1


def test_empty():
    assert rabin_karp_search("", "test") == -1
    assert rabin_karp_search("test", "") == -1


def test_almost_match():
    assert rabin_karp_search("abracadabra", "dab") == 6


def test_repeated_patterns():
    assert rabin_karp_search("aaaaa", "aaa") == 0
