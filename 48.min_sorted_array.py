def sortedarray(nums):
    n=len(nums)
    mini=float("inf")
    for i in range(0,n):
        mini=min(nums[i],mini)
    return mini
nums=[11,15,20,1,4,5,6,8,9,10]
print(sortedarray(nums))