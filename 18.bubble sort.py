def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

user_input=input('Enter the numbers separated by spaces: ')
arr=list(map(int, user_input.split()))
bubble_sort(arr)
print('The sorted array is: ', arr)
