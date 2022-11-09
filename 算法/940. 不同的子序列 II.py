class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1e9 + 7
        n = len(str)
        dp = [0]
        for i, s in enumerate(str, 1):
            dp[i] = dp[i-1]