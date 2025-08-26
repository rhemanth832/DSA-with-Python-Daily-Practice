nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]

# Get the number of rows and columns
rows = len(nums)
cols = len(nums[0])

# Iterate over each element and print
for i in range(rows):
    for j in range(cols):
        print(nums[i][j], end=" ")
    print()  # Move to next line after each row

# Upper in Matrix
nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]
rows = len(nums)
cols = len(nums[0])
for i in range(rows):
    for j in range(cols):
        if j>=i:
            print(nums[i][j], end="  ")
        else:
            print("*", end="  ")
    print()

# Lower in Matrix
nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]
rows = len(nums)
cols = len(nums[0])
for i in range(rows):
    for j in range(cols):
        if i>=j:
            print(nums[i][j], end="  ")
        else:
            print("*", end="  ")
    print()

# Diagonal in Matrix
nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]
rows = len(nums)
cols = len(nums[0])
for i in range(rows):
    for j in range(cols):
        if i==j:
            print(nums[i][j], end="  ")
        else:
            print("*", end="  ")
    print()

#Transpose of matrix
nums = [[5, 20, 3],
        [7, -10, 9],
        [1, -52, 6]]
rows = len(nums)
cols = len(nums[0])
result=[[0]*rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i]=nums[i][j]
print(result)
