def transpose(mat):
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

mat = [[1, 2],
        [3, 4],
        [5, 6]]

print("normal: " + repr(mat))

print("transposed: " + repr(transpose(mat)))

