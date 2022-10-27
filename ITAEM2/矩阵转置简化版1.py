import copy

row = int(input("请输入矩阵的规模n："))
col = row
matrix = []
for i in range(row):
    print("请输入第", (i+1), "行数字，并用空格隔开数字:")
    matrix.append([int(x) for x in input().split(" ")])

print("你输入的矩阵为：")
for i in range(row):
    print(matrix[i])

# 转置
M = int(input("请输入小青蛙转置的次数M："))

matrix_copy = copy.deepcopy(matrix)


def turn(count):
    for i in range(row):
        for j in range(col):
            matrix[i][j] = matrix_copy[j][i]
    # print("经过", count, "次顺时针旋转后的矩阵为：")
    # for i in range(row):
    #     print(matrix[i])


real_M = M % 4
for i in range(real_M):
    turn(i+1)
    matrix_copy = copy.deepcopy(matrix)

print("通过", M, "次转置后的矩阵为：")
for i in range(row):
    print(matrix[i])
