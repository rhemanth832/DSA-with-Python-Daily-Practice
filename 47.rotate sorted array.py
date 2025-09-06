def sortedarray(nums):

    target=8
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1
nums=[11,15,20,1,4,5,6,8,9,10]
print(sortedarray(nums))