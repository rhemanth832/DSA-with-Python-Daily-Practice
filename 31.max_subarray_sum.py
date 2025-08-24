def max_subarray(arr):
    n=len(arr)
    curr_sum=max_sum=arr[0]
    for i in range(1,n):
        if curr_sum +arr[i] > arr[i]:
            curr_sum=curr_sum+arr[i]
        else:
            curr_sum=arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum
h=list(map(int, input('Enter numbers separated by spaces: ').split())) # 1 -2 3 4 -1 2 1 -5 4
print(max_subarray(h))