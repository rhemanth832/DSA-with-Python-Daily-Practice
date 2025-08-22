arr=list(map(int, input('Enter numbers seperated by commas: ').split(',')))
target=int(input('Enter the number to be searched from array: '))
if target in arr:
    print('Number is found in array at: ',arr.index(target))
else:
    print('No is not found in Array')