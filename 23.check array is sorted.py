def array_sort(nums):
    n=len(nums)
    for i in range(n-1):
        if (nums[i]>nums[i+1]):
            return False
    return True
r=list(map(int, input('Enter the numbers seperated by commas: ').split(',')))
print(array_sort(r))