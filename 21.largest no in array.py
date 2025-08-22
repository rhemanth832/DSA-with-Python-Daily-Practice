def largest_no(nums):
    largest=nums[0]
    n=len(nums)
    for i in range(1,n):
        largest=max(largest,nums[i])
    return largest
h=list(map(int, input('Enter the numbers seperated by commas: ').split(',')))
print('Largest Number in the array is: ',largest_no(h))