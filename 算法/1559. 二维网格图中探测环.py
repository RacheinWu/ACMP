from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
        self.part = n

    def Find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.Find(self.parent[x])

    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True

    """
        是否在同一个集合中
    """
    def is_samepart(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)

    """
        获取一个集合的元素数量
    """
    def get_partsize(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]

##########################################################################################################
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R, C = len(grid), len(grid[0])
        UF = UnionFind(R * C)
        for r in range(R):
            for c in range(C):
                ID = r * C + c
                if 0 <= r - 1 < R and grid[r - 1][c] == grid[r][c]:
                    ID_up = (r - 1) * C + c
                    if UF.is_samepart(ID, ID_up):
                        return True
                    else:
                        UF.Union(ID, ID_up)

                if 0 <= c - 1 < C and grid[r][c - 1] == grid[r][c]:
                    ID_left = r * C + c - 1
                    if UF.is_samepart(ID, ID_left):
                        return True
                    else:
                        UF.Union(ID, ID_left)
        return False
