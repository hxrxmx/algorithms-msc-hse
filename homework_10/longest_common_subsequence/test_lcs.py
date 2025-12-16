from homework_10.longest_common_subsequence.lcs import longest_common_subsequence


def test_basic_example():
    assert longest_common_subsequence("aggtab", "gxtyayb") == "gtab"


def test_identical_strings():
    assert longest_common_subsequence("abc", "abc") == "abc"


def test_no_common_subsequence():
    assert longest_common_subsequence("abc", "xyy") == ""


def test_one_empty_string():
    assert longest_common_subsequence("", "akjd") == ""
    assert longest_common_subsequence("aojfj", "") == ""


def test_subsequence_as_substring():
    assert longest_common_subsequence("aananas", "nas") == "nas"
