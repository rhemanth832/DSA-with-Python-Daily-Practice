matrix = [
  [1, 2, 3],
  [4, 0, 6],
  [7, 8, 9]
]
r=len(matrix)
c=len(matrix[0])
rtrack=[0 for _ in range(r)]
ctrack=[0 for _ in range(c)]
for i in range(0,r):
    for j in range(0, c):
        if matrix[i][j]==0:
            rtrack[i]=-1
            ctrack[j]=-1

for i in range(0,r):
    for j in range(0, c):
        if rtrack[i]==-1 or ctrack[j]==-1:
            matrix[i][j]=0

print(matrix)

