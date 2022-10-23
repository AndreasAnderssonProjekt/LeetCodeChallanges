def two_sum(nums, target):
    dict = {}
    for i in range(len(nums)):
        dict[target - nums[i]] = i

    for key in dict.keys():
        if nums[dict[target - key]] in dict:
            return [dict[key], dict[target - key]]
    return -1
