from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def dfs(i: int, j: int, is_right: bool):
            # 边界：
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return
            # 碰到0:
            if matrix[i][j] == 0:
                # 判断方向：
                if is_right:
                    self.zuiyou = min(self.zuiyou, j)
                else:
                    self.zuixia = min(self.zuixia, i)
            # 继续往深处走：
            # right:
            dfs(i, j+1, True)
            dfs(i+1, j, False)



        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.zuiyou = j
                    self.zuixia = i
                    dfs(i, j, False)
                    max_area = max(max_area, (self.zuiyou-j)*(i-self.zuixia))
        return max_area