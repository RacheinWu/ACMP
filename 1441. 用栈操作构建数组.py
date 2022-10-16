from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        for j in range(1, n+1):
            if j == len(target):
                break
            if target[i] == j:
                res.append("Push")
                i += 1
            else:
                res.append("Push")
                res.append("Pop")
        return res
