def subset_sum(nums, target):
    dp = [False]*(target+1)
    dp[0] = True
    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]
    return dp[target]

# Example
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(nums, target))  # True
