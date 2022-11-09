from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid: List[List[int]], row: int, col: int) -> bool:
            # 如果在边界那么就不行了，return False
            # 不用检测数组是否越界，因为只要最多判断边界情况就可以直接return了
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False
            # 如果是海，那么就代表符合题意，return True
            if grid[row][col] == 1:
                return True
            # 如果是陆地，那么标记已访问，只要标记为1（海）即可：
            grid[row][col] = 1
            r1 = dfs(grid, row + 1, col)
            r2 = dfs(grid, row - 1, col)
            r3 = dfs(grid, row, col + 1)
            r4 = dfs(grid, row, col - 1)
            return r1 and r2 and r3 and r4

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and dfs(grid, i, j):
                    res += 1
        return res
