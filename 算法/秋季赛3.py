from collections import Counter
from typing import List


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans = left = 0
        c = Counter()
        for right, x in enumerate(flowers):
            # print(right, x)
            c[x] += 1
            while c[x] > cnt:
                c[flowers[left]] -= 1
                left += 1
            ans += right - left + 1


so = Solution()
so.beautifulBouquet(flowers=[1,2,3,2], cnt=1)