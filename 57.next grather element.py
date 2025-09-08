def nextLargerElement(arr, n):
    return [next((arr[j] for j in range(i+1, n) if arr[j] > arr[i]), -1) for i in range(n)]
arr = [4, 5, 2, 25]
print(nextLargerElement(arr, len(arr)))