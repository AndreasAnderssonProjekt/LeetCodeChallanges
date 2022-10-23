def houseRobber(nums):
    if len(nums) == 1:
        return nums[0]
    
    opt = [0] * len(nums)
    opt[0] = nums[0]
    opt[1] = max(nums[0], nums[1])

    for i in range(1,len(nums)):
        opt[i] = max(opt[i-1], opt[i-2] + nums[i])

    return opt[-1]
