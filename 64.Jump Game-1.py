def farjump(nums):
    farthest=0
    n=len(nums)
    for i in range(n):
        if i >farthest:
            return False
        farthest=max(farthest, i+nums[i])
    return True
print(farjump([2,3,1,1,4]))