from typing import List




class Solution:



    def closedIsland(self, grid: List[List[int]]):
        def dfs(grid, i, j)->bool:
            if isOut(grid, i, j):
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            return dfs(grid, i+1, j) and dfs(grid, i-1, j) and dfs(grid, i, j+1) and dfs(grid, j-1)


        def isOut(grid: List[List[int]], i: int, j: int)->bool:
            pass

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(grid, i, j)
                    res += 1