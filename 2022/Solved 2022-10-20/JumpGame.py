def jumpGame(nums):
    n = len(nums)
    best_sol = nums[0]

    for i in range(n):
        if best_sol >= n - 1:
            return True

        if i > best_sol:
            return False

        if nums[i] + i > best_sol:
            best_sol = nums[i] + i
