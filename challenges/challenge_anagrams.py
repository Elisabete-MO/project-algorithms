def mergesort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left_half = s[:mid]
    right_half = s[mid:]

    left_half = mergesort(left_half)
    right_half = mergesort(right_half)

    sorted_lst = merge(left_half, right_half)

    return sorted_lst


def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def is_anagram(first_string, second_string):
    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    first_string = mergesort(first_string)
    second_string = mergesort(second_string)
    
    first_string = ''.join(first_string)
    second_string = ''.join(second_string)

    if not first_string or not second_string:
        return (first_string, second_string, False)

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)

# if __name__ == "__main__":
#     word = 'Roma'
#     print(is_anagram(word, 'amor')) #TRUE
#     print(is_anagram(word, 'roma')) #TRUE
#     print(is_anagram(word, 'not')) #FALSE
#     print(is_anagram(word, 'Amor')) #TRUE
