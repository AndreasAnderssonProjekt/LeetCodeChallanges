def combinationSum(nums, target):
    if target == 0:
        return 1

    sol = 0

    for num in nums:
        if (target >= num):
            sol += combinationSum(nums, target - num)

    return sol
