def longestConsecutive(nums):
    nums = set(nums)
    opt = 0

    for num1 in nums:
        if num1 - 1 not in nums:
            streak = 1
            num2 = num1 + 1

            while num2 in nums:
                num2 += 1
                streak += 1

            if opt < streak:
                opt = streak

    return opt
