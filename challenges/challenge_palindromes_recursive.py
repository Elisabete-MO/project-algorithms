def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if high_index <= 1:
        return True
    elif word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# if __name__ == "__main__":
    # print(is_palindrome_recursive('ANA')) #TRUE
    # print(is_palindrome_recursive('SOCOS')) #TRUE
    # print(is_palindrome_recursive('REVIVER')) #TRUE
    # print(is_palindrome_recursive('COXINHA')) #FALSE
    # print(is_palindrome_recursive('AGUA')) #FALSE
