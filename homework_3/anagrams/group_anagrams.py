from collections import defaultdict


def group_anagrams(strings):
    strings_dict = defaultdict(list)
    for string in strings:
        bag_of_letters = [0] * 26
        for letter in string:
            bag_of_letters[ord(letter) - ord("a")] = 1
        strings_dict[tuple(bag_of_letters)].append(string)
    return list(strings_dict.values())
