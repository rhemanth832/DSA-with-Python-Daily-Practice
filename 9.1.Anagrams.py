def count_frequencies(arr):
    freq_map = {}
    for i in range(len(arr)):
        if arr[i] in freq_map:
            freq_map[arr[i]] += 1
        else:
            freq_map[arr[i]] = 1
    return freq_map

nums = [5, 6, 7, 7, 1, 9, 11, 1, 1, 5, 1]
nums2= [6, 5, 1, 7, 7, 1, 1, 11, 5, 9, 1]
result = count_frequencies(nums)
result2 = count_frequencies(nums2)
print(result)
print(result2)
if result==result2:
    print('Anagrams')
else:
    print('Not Anagrams')