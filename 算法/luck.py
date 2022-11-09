import math

arr = input().split()
n = int(arr[0])
k = arr[1]


def isSu(num: int) -> bool:
    j = int(math.sqrt(num+1))
    while j > 1:
        if num % j == 0:
            return False
        j -= 1
    return True

res = 0
# 先求n内的所有素数：
for i in range(2,n):
    if isSu(i):
        if k not in str(i):
            res += 1

print(res)
