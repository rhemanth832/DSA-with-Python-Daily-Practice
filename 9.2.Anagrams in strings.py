nums='heart'
nums1='earth'
print(nums)
print(nums1)
d1={}
d2={}
for i in nums:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
for i in nums1:
    if i in d2:
        d2[i]+=1
    else:
        d2[i]=1
if d1==d2:
    print('Anagrams')
else:
    print('Not Anagrams')
print(d2['r'])
