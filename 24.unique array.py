arr=list(map(int, input('Enter the numbers seperated by commas: ').split(',')))
unique=sorted(set(arr))
print(unique)