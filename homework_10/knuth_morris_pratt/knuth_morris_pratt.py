def build_prefix_table(pattern):
    table = [0 for _ in range(len(pattern))]
    prefix_length = 0
    current_index = 1

    while current_index < len(pattern):
        if pattern[current_index] == pattern[prefix_length]:
            prefix_length += 1
            table[current_index] = prefix_length
            current_index += 1

        elif prefix_length > 0:
            prefix_length = table[prefix_length - 1]

        else:
            table[current_index] = 0
            current_index += 1
    return table


def knuth_morris_pratt_search(text, pattern):
    if len(text) * len(pattern) == 0:
        return -1

    prefix_table = build_prefix_table(pattern)

    text_index = 0
    pattern_index = 0
    while text_index < len(text):
        if pattern[pattern_index] == text[text_index]:
            pattern_index += 1
            text_index += 1

            if pattern_index == len(pattern):
                return text_index - pattern_index

        elif pattern_index != 0:
            pattern_index = prefix_table[pattern_index - 1]
        else:
            text_index += 1
    return -1
