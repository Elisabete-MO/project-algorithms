def find_duplicate(nums):
    if not nums or \
      any(isinstance(num, str) for num in nums) or \
      any(num < 0 for num in nums):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False

# if __name__ == "__main__":
#     print(find_duplicate([1, 3, 4, 2, 2])) # saída: 2
#     print(find_duplicate([3, 1, 3, 4, 2])) # saída: 3
#     print(find_duplicate([1, 1])) # saída: 1
#     print(find_duplicate([1, 1, 2])) # saída: 1
#     print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8])) # saída: 7
#     print(find_duplicate(['3', 1, 2, 4, 6, 5, 7, 7, 7, 8])) # saída: FALSE
#     print(find_duplicate([])) # saída: FALSE
#     print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 8])) # saída: FALSE
