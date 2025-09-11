class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b

# Example
print(Solution().climbStairs(5))  # Output: 8
