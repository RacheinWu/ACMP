class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        if length == 0:
          return 0
        dp = [0] * length
        for i in range(1, length):
            if s[i] == ')':
                left_index = i - dp[i-1] - 1
                if left_index >= 0 and s[left_index] == '(':
                    dp[i] = dp[i-1] + 2
                    if left_index > 0:
                        dp[i] += dp[left_index-1]
        return max(dp)