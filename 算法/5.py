n = int(input())
res = []
result = 1
res.append(result)
for i in range(n):
    result += 1
    for j in range(i+1):
        res.append(result)
        result += 2
    res.append(result)
    if len(res) > n:
        break

print(res[n-1])
