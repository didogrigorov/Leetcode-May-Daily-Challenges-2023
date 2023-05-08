from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    total_sum = 0
    n = len(mat)

    for i in range(n):
        total_sum += mat[i][i]
        total_sum += mat[i][n - 1 - i]

    if n % 2 != 0:
        total_sum -= mat[n // 2][n // 2]


    return total_sum

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print(diagonalSum(mat))