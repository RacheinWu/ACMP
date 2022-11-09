from collections import deque, defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        index1, index2, res = 0, 0, 0
        tem = deque()
        for index2 in range(len(fruits)):
            if len(tem) < 2:
                tem.append(fruits[index2])
            print("tem=", tem)
            if fruits[index2] in tem:
                print("【在】fruits[index2]=", fruits[index2])
                continue
            print("【不在】fruits[index2]=", fruits[index2])
            # 记录最大距离
            res = max(res, index2 - index1 + 1)
            print("更新：", res)
            # 队列出队：
            tem.popleft()
            # 新出现的数字进行加入队列
            tem.append(fruits[index2])
            # index1 = index2 - 1：
            index1 = index2 - 1
        return max(index2 - index1 + 1, res)




so = Solution()
print(so.totalFruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
