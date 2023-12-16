"""
Given an integer array nums, return an array answer such that answer[i]
 is equal to the product of all the elements of nums except nums[i].
"""

def productExceptSelf(nums):
    left_product = [1]
    right_product = [1]

    for i in range(1,len(nums)):
        left_product.append(left_product[i-1] * nums[i-1])
        right_product.append(right_product[i - 1] * nums[len(nums)- i])

    result = []
    for i in range(len(nums)):
        result.append(left_product[i] * right_product[len(nums) - 1 - i])

    return result
