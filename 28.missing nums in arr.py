def missing_nums(nums):
    n=len(nums)
    for i in range(n+1):
        if i not in nums:
            return i
h=list(map(int, input('Enter numbers seperated by commas: ').split(',')))
print(missing_nums(h))
