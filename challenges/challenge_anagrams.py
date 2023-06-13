def quicksort(s, low, high):
    if low < high:
        pivot_index = partition(s, low, high)
        quicksort(s, low, pivot_index - 1)
        quicksort(s, pivot_index + 1, high)
    return ''.join(s)


def partition(s, low, high):
    pivot = s[high]
    i = low - 1

    for j in range(low, high):
        if s[j] <= pivot:
            i += 1
            s[i], s[j] = s[j], s[i]

    s[i + 1], s[high] = s[high], s[i + 1]
    return i + 1


def is_anagram(first_string, second_string):

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    quicksort(first_string, 0, len(first_string) - 1)
    quicksort(second_string, 0, len(second_string) - 1)

    first_string = ''.join(first_string)
    second_string = ''.join(second_string)

    if not first_string or not second_string:
        return (first_string, second_string, False)

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)

# if __name__ == "__main__":
#     word = 'dcba'
#     print(is_anagram(word, 'abcd'))
#     print(is_anagram(word, 'bacd'))
#     print(is_anagram(word, 'not'))
#     print(is_anagram('amor', 'arMo'))
