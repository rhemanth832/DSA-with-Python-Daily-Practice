arr=list(map(int, input('Enter the number seperated by commas: ').split(',')))
for _ in range(arr.count(0)):
    arr.remove(0)
    arr.append(0)
print(arr)