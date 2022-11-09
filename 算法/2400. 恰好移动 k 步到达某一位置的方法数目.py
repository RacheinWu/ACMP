class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        def func(x: int, left: int) -> int:
            if abs(x - endPos) > left:
                return 0
            if left == 0:
                return 1
            return (func(x - 1, left - 1) + func(x + 1, left - 1)) % MOD
        return func(startPos, k)