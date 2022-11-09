from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # 用hash表去记录起点和终点
        map = [None for _ in range(26)]
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if map[index] is None:
                # 还没访问
                map[index] = i
            elif map[index] is not None:
                # 首次访问过了
                # 此时为终点，记录位置
                map[index] = i - map[index] - 1
        print(map)
        p1 = 0
        while p1 < len(distance):
            if map[p1] is None:
                p1 += 1
                continue
            if map[p1] != distance[p1]:
                return False
            p1 += 1
            print(p1)
        return True


so = Solution()
r = so.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(r)

