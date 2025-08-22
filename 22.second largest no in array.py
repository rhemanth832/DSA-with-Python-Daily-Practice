h=list(map(int, input('Enter the numbers seperated by commas: ').split(',')))
h.sort()
print('Sorted array',h)
print("2nd Largest Number in array is:", h[-2])