from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        tmp = []
        prefix = ""
        s0 = strs[0]
        min_length = min(len(x) for x in strs)
        for i in range(min_length):
            for j in range(n):
                tmp.append(strs[j][i])
            if len(set(tmp)) == 1:
                prefix += s0[i]
                tmp = []
            else:
                break
        return prefix
