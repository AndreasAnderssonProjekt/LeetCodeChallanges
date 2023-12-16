def findSmallestPositive(nums):

    targets = []
    for i in range(len(nums)+2):
        targets.append(i)

    for i in range(len(nums)):
        if nums[i] > 0 and nums[i] < len(targets):
            print(nums[i])
            targets[nums[i]] = 0

    for i in range(len(targets)):
        if targets[i] > 0:
            return targets[i]
    return targets[-1]
