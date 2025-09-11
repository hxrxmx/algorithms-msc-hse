def is_palindrome(num):
    num_string = str(num)
    return num_string == num_string[::-1]
