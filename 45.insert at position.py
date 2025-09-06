def insert_mid(nums, target):
    n=len(nums)
    lb=n
    low=0
    high=n-1
    while low <= high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
h=list(map(int, input('Enter no by spaces: ').split())) # 1 3 4 5 8 9 14 15 19 20 21
target = int(input("Enter target number: ")) # target = 16
print(insert_mid(h, target))

