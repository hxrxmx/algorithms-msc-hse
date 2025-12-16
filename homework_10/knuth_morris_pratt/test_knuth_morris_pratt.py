from homework_10.knuth_morris_pratt.knuth_morris_pratt import knuth_morris_pratt_search


def test_match():
    assert knuth_morris_pratt_search("huuuuuuh", "uh") == 6
    assert knuth_morris_pratt_search("huuuuu", "hu") == 0


def test_no_match():
    assert knuth_morris_pratt_search("abcdefg", "xyz") == -1


def test_repetitive_pattern():
    assert knuth_morris_pratt_search("abxabcabcaby", "abcaby") == 6


def test_long_pattern():
    assert knuth_morris_pratt_search("shorttext", "looooooong pattern") == -1


def test_empty():
    assert knuth_morris_pratt_search("text", "") == -1
    assert knuth_morris_pratt_search("", "pattern") == -1
