N = int(input("输入第一行一个正整数N (0<N<10)"))
matrix = []
for i in range(N):
    matrix.append(input().split(" "))

M = int(input("正整数M (0<=M<=10000):"))
M = M % 3
matrix_1 = matrix.copy()
def turn():
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                # matrix[i][j] = matrix_1[][]
                pass
            else:
                matrix[i][j] = matrix_1[N - j - 1][N - i - 1]
            print(N-j-1, N-i-1)
            print(matrix)
    print()

print(matrix)
for _ in range(M):
    turn()
    matrix_1 = matrix.copy()

