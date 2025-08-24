nums=[1,1,0,1,0,1,1,1,1,0,1,1]
count=0
maxi=0
n=len(nums)
for i in range(0,n):
    if nums[i]==1:
        count+=1
    else:
        maxi=max(maxi,count)
        count=0

print(maxi)
