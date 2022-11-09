from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for index, val in enumerate(nums):
            if val == original:
                original *= 2
        return original
