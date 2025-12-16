def longest_common_subsequence(string_1, string_2):
    length_1 = len(string_1)
    length_2 = len(string_2)

    dp = [[0] * (length_2 + 1) for _ in range(length_1 + 1)]

    for row in range(1, length_1 + 1):
        for col in range(1, length_2 + 1):
            if string_1[row - 1] == string_2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    result_characters = []
    current_row, current_col = length_1, length_2

    while current_row > 0 and current_col > 0:
        if string_1[current_row - 1] == string_2[current_col - 1]:
            result_characters.append(string_1[current_row - 1])
            current_row -= 1
            current_col -= 1
        elif dp[current_row - 1][current_col] > dp[current_row][current_col - 1]:
            current_row -= 1
        else:
            current_col -= 1

    return "".join(reversed(result_characters))
