def rearrange_ns(nums):
    pos=[x for x in nums if x>=0]
    neg=[x for x in nums if x<0]
    result=[]

    for p, n in zip(pos, neg):
        result.append(p)
        result.append(n)
        # print remaining
    result.extend(pos[len(neg):])
    result.extend(neg[len(pos):])

    return result
nums = [3, -2, 5, -7, -1, 4]
print(rearrange_ns(nums))  