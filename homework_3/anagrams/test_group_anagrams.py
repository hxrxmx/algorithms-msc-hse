from homework_3.anagrams.group_anagrams import group_anagrams


def normalize(list_of_lists):
    return sorted([sorted(g) for g in list_of_lists])


def test_group_anagrams():
    assert group_anagrams([]) == []
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["ab", "ba"]) == [["ab", "ba"]]

    assert normalize(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    ) == normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
