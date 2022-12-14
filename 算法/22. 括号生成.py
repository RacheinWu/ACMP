from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 路径字符串【组合】
            :param left: 左括号剩余个数
            :param right: 右括号剩余个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                # jianzhi
                return
            if left > 0:
                dfs(cur_str + '(', left-1, right)
            if right > 0:
                dfs(cur_str+')', left, right-1)

        dfs(cur_str, n, n)
        return res
