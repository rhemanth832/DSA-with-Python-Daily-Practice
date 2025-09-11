#House Robber-1 or 2 same

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev1 = prev2 = 0
            for num in houses:
                prev1, prev2 = max(prev2 + num, prev1), prev1
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Example
nums = [2,3,2]
print(Solution().rob(nums))  # Output: 3

nums = [1,2,3,1]
print(Solution().rob(nums))  # Output: 4
