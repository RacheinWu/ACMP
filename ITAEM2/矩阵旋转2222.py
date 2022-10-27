from copy import deepcopy
from typing import List


def turn(arr: List[List[int]], n: int):
    copy_matrix = deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = copy_matrix[j][n - 1 - i]


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(matrix)):
    print(matrix[i])

M = 4
x = M % 4
for i in range(x):
    turn(matrix, 2)
# turn(matrix, 2)
print("--------------------")
for i in range(len(matrix)):
    print(matrix[i])
