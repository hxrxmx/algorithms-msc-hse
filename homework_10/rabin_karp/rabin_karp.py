def rabin_karp_search(text, pattern, alphabet_base=512, prime_modulus=100):
    text_length = len(text)
    pattern_length = len(pattern)

    if pattern_length > text_length or text_length * pattern_length == 0:
        return -1

    high_order_weight = 1
    for _ in range(pattern_length - 1):
        high_order_weight = (high_order_weight * alphabet_base) % prime_modulus

    pattern_hash = 0
    window_hash = 0
    for index in range(pattern_length):
        pattern_hash = (
            alphabet_base * pattern_hash + ord(pattern[index])
        ) % prime_modulus

        window_hash = (alphabet_base * window_hash + ord(text[index])) % prime_modulus

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == window_hash:
            if text[i : i + pattern_length] == pattern:
                return i

        if i < text_length - pattern_length:
            window_hash = (
                window_hash - ord(text[i]) * high_order_weight
            ) % prime_modulus

            window_hash = (
                window_hash * alphabet_base + ord(text[i + pattern_length])
            ) % prime_modulus

    return -1
