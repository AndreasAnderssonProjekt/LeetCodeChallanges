def search(nums,target):
   rotation = findSmallest(nums)
   i = 0
   j = len(nums) - 1
   while i <= j:
       mid = (i + j) // 2
       rotated_mid = (mid + rotation) % (len(nums) - 1)
       if nums[rotated_mid] > target:
           j = mid - 1
       elif nums[rotated_mid] < target:
           i = mid + 1
       else:
           return rotated_mid
   return -1

def findSmallest(nums):
    i = 0
    j = len(nums) - 1
    mid = (i + j) // 2

    while i < j:
        if nums[mid] < nums[j]:
            j = mid
        else:
            i = mid + 1
        mid = (i + j) // 2

    return i
