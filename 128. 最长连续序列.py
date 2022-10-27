import collections
from typing import List


class UnionFind:

    def __init__(self, nums):
        self.parent = {num: nums for num in nums}
        self.count = collections.defaultdict(lambda: 1)
        print(self.count)

    def union(self, x: int, y: int) -> int:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_y == parent_x:
            return self.count[parent_y]
        self.parent[parent_x] = parent_y
        self.count[parent_y] += self.count[parent_x]
        return self.count[parent_y]

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.find(self.parent[x])
        return x


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        res = 1
        while len(nums_set) > 0:
            now = nums_set.pop()
            now_right = now + 1
            now_left = now - 1
            while now_left in nums_set:
                nums_set.remove(now_left)
                now_left -= 1
            while now_right in nums_set:
                nums_set.remove(now_right)
                now_right += 1
            res = max(res, now_right - now_left - 1)
        return res