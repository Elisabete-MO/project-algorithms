def is_palindrome_iterative(word):
    if not word:
        return False

    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

# if __name__ == "__main__":
#     print(is_palindrome_iterative('ANA')) #TRUE
#     print(is_palindrome_iterative('SOCOS')) #TRUE
#     print(is_palindrome_iterative('REVIVER')) #TRUE
#     print(is_palindrome_iterative('COXINHA')) #FALSE
#     print(is_palindrome_iterative('AGUA')) #FALSE
