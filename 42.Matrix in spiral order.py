def spiralOrder(matrix):
    result = []
    while matrix:

        result += matrix[0]
        matrix = matrix[1:]

        matrix = list(zip(*matrix))[::-1]
    return result


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiralOrder(mat))
