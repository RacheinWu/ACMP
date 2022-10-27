n, i, j = 0, 0, 0
n = int(input("请问你想打印几行呢？"))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i - 1 + 1):
        print("*", end="")
    print()
# xiaban
for i in range(n - 1):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * ((n - 1) - i) - 1):
        print("*", end="")
    print()