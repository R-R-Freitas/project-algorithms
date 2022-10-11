def finder(nums):
    n = 0
    while n < len(nums):
        if nums[n] == nums[n + 1]:
            return nums[n]
        n += 1


def find_duplicate(nums):
    try:
        if len(nums) < 2:
            return False
        nums.sort()
        if nums[0] < 1:
            return False
        return finder(nums)
    except (TypeError, IndexError):
        return False
