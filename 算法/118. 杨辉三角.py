from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows == 3:
            return [[1], [1, 1], [1, 2, 1]]
        res = [[1], [1, 1], [1, 2, 1]]
        for i in range(3, numRows):
            cur = [1]
            for j in range(1, i):
                cur.append(res[i - 1][j - 1] + res[i - 1][j])
            cur.append(1)
            res.append(cur)
        return res


so = Solution()
print(so.generate(5))
