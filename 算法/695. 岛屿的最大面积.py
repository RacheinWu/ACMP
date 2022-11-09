from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(row: int, col: int) -> int:
            # 边界 or 海洋：
            if row < 0 or col < 0 or row >= n or col >= m or grid[i][j] == 0:
                return 0
            # 记录已访问
            grid[i][j] = 0
            return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1) + 1

        max_area = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
