# from PIL import Image
# import numpy as np
#
# im = np.array(Image.open('C:/Users/Rache/Pictures/Saved Pictures/。。/6be7d5ffgy1g5nr338f5uj20qo0qotef.jpg'))
# copy = im.copy()
# # 转置
# arr = im.shape
# for i in range(arr[0]):
#     for j in range(arr[1]):
#         for z in range(arr[2]):
#             im[i][j][z] = copy[j][arr[0]-i-1][z]
#
#
# Image.fromarray(im).save('./lena_save_pillow_gray.jpg')

import copy

row = int(input("请输入矩阵的规模n："))
# col = int(input("请输入矩阵的列数："))
col = row
matrix = []
for i in range(row):
    print("请输入第", (i+1), "行数字，并用空格隔开数字:")
    matrix.append([int(x) for x in input().split(" ")])

print("你输入的矩阵为：")
for i in range(row):
    print(matrix[i])

# 顺时针旋转
M = int(input("请输入顺时针旋转的次数："))

matrix_copy = copy.deepcopy(matrix)


def turn(count):
    for i in range(row):
        for j in range(col):
            # matrix[i][j] = matrix_copy[j][row-i-1]  # 逆时针
            matrix[i][j] = matrix_copy[row-j-1][i]  # 顺时针
    # print("经过", count, "次顺时针旋转后的矩阵为：")
    # for i in range(row):
    #     print(matrix[i])


real_M = M % 4
for i in range(real_M):
    turn(i+1)
    matrix_copy = copy.deepcopy(matrix)

print("通过", M, "次顺时针旋转后的矩阵为：")
for i in range(row):
    print(matrix[i])
