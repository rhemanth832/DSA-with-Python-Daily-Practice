class Solution():
    def longestOnes(self, nums, k):
        left = 0
        zero_count = 0
        maxi = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # Output: 6