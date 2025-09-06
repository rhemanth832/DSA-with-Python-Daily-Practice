from itertools import combinations
def fourSum(nums, target):
    res = set()
    for a, b, c, d in combinations(nums, 4):
        if a + b + c + d == target:
            res.add(tuple(sorted([a, b, c, d])))
    return list(res)
print(fourSum([1, 0, -1, 0, -2, 2], 0))
