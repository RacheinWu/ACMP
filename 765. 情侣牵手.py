from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        pos = {}
        for i in range(N):
            pos[row[i]] = i

        res = 0
        for i in range(0, N-1, 2):
            pairperson = row[i] ^ 1
            nextperson = row[i+1]
            if pairperson == nextperson:
                continue
            pairlocation = pos[pairperson]





#

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        pos = {}
        for i in range(N):
            pos[row[i]] = i
        res = 0
        for i in range(0, N-1, 2):
            pairperson = row[i]^1
            nextperson = row[i+1]
            if nextperson == pairperson:
                continue
            pairlocation = pos[pairperson]
            row[pairlocation], pos[nextperson] = nextperson, pairlocation
            res += 1
        return res