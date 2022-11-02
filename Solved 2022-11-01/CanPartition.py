"""
Given a non-empty array nums containing only positive integers, find if the array can 
be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""
def canPartition(nums):
    s = sum(nums)

    if s % 2 != 0:  # Can't partition if sum is odd.
        return False

    s = s // 2

    opt = [[False for j in range(s + 1)] for i in range(len(nums) + 1)]
    opt[0][0] = True
    for i in range(1, len(nums) + 1):
        opt[i][0] = True

    for j in range(1, s + 1):
        opt[0][j] = False

    for i in range(1, len(nums) + 1):
        for j in range(1, s + 1):
            opt[i][j] = opt[i - 1][j]

            if j - nums[i - 1] >= 0:
                opt[i][j] = opt[i-1][j - nums[i - 1]] or opt[i][j]

    return opt[len(nums)][s]
