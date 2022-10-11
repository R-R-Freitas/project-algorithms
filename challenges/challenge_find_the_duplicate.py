def find_duplicate(nums):
    # try:
    #     if len(nums) < 2 or min(nums) < 0:
    #         return False
    #     if nums[0] in nums[1:]:
    #         return nums[0]
    #     else:
    #         return find_duplicate(nums[1:])
    # except TypeError:
    #     return False
    try:
        if len(nums) < 2 or min(nums) < 0:
            return False
        for i in range(len(nums)):
            if nums[i] in nums[(i+1):]:
                return nums[i]
        return False
    except TypeError:
        return False
