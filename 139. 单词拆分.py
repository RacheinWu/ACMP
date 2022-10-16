from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        memo = []

        def can_break(start) -> bool:
            if start == n:
                return True
            if memo[start] is not None:
                return memo[start]
            for i in range(start+1, n+1):
                if s[start:i] in wordSet and can_break(i):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return can_break(0)
