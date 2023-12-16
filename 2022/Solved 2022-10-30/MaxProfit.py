def maxProfit(nums):
    buy = nums[0]
    max_profit = 0
    for i in range(1,len(nums)):
        sell = nums[i]
        profit = sell - buy
        if profit > max_profit:
            max_profit = profit
        if profit < 0:
            buy = nums[i]
    return max_profit
