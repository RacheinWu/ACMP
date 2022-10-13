from functools import reduce
from operator import or_
from typing import List, Counter


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        dic = dict()
        res = 0
        length = len(demand)
        for i in range(length):
            sub = dict()
            for j in range(len(demand[i])):
                if demand[i][j] not in sub:
                    sub[demand[i][j]] = 1
                else:
                    sub[demand[i][j]] += 1
            for k, v in sub.items():
                if k not in dic:
                    dic[k] = v
                    res += v
                elif v > dic[k]:
                    res += v - dic[k]
                    dic[k] = v
        return res
