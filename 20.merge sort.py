def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge sorted halves using simple list operations
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))  # pop the first element
        else:
            result.append(right.pop(0))
    # Add any remaining elements
    result.extend(left)
    result.extend(right)
    return result
# Input and output
nums = list(map(int, input("Enter numbers separated by commas: ").split(',')))
sorted_nums = merge_sort(nums)
print("Sorted array:", sorted_nums)