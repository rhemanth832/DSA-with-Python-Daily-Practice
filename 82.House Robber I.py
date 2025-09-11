class Solution(object):
    def rob(self, nums):
        prev1, prev2 = 0, 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp
        return prev1
nums = [2,7,9,3,1]
print(Solution().rob(nums))  # Output: 12
