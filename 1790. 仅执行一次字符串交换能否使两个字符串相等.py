class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n, a, b = len(s1), -1, -1
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if a == -1:
                a = i
            elif b == -1:
                b = i
            else:
                return False
        if a == -1:
            return True
        if b == -1:
            return False
        print(a, b)
        return s1[a] == s2[b] and s1[b] == s2[a]


so = Solution()
so.areAlmostEqual(s1 = "bank", s2 = "kanb")