def sort_nums(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left, right = sort_nums(nums[:mid]), sort_nums(nums[mid:])
    return merge(left, right, nums.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def finder(nums):
    n = 0
    while n < len(nums):
        if nums[n] == nums[n + 1]:
            return nums[n]
        n += 1


def find_duplicate(nums):
    try:
        sorted_nums = sort_nums(nums)
        if len(nums) < 2 or sorted_nums[0] < 1:
            return False
        return finder(sorted_nums)
    except (TypeError, IndexError):
        return False
