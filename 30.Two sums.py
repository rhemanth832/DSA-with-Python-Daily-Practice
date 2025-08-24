nums=[2,7,11,15]
output=[]
target=9
sum=0
n=len(nums)
for i in range(0,n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            output.append(i)
            output.append(j)
            break
print('Output: ',output)

#(OR)
nums=[2,7,11,15]
output=[]
target=9
sum=0
dic= {}
n=len(nums)
for i in range(0,n):
    diff=target-nums[i]
    if diff in dict:
        output.append(i)
        output.append(dic[diff])
        print('Output: ',output)
    dict[nums[i]]=i



