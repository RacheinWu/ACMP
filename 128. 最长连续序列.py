from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                current_length = 1
                current_num = num
                while current_num+1 in nums_set:
                    current_length += 1
                    current_num += 1
                max_length = max(current_length, max_length)
        return max_length
