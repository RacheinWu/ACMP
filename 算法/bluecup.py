from collections import deque

t = int(input())
t = int(t/60)
if t <= 3:
    print(t)
else:
    temp = deque([1, 2, 3])
    # 从第四分钟开始
    for i in range(4, int(t)+1):
        temp.append((temp[i-2] + temp[i-1] + temp[i]) % 425)
        # temp.popleft()

    print(temp[int(t)] % 425)