from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(self, grid, i, j)

    def dfs(self, grid: List[List[int]], r, c):
        if self.judge(grid, r, c):
            return
        if grid[r][c] == 2:
            return
        grid[r][c] = 2
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)


    def judge(self, grid: List[List[int]], r, c) -> bool:
        return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
