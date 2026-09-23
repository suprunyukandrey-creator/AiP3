def sum_matr(A, B):
    f = []
    stroki = len(A[0])
    stolbci = len(A)
    for i in range(stroki):
        f.append([])
        for j in range(stolbci):
            f[i].append(A[i][j] + B[i][j])
    return f
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
print(sum_matr(A, B))
