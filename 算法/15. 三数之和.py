from typing import List


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res = []
        for a in range(len(nums) - 2):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b, c = a + 1, len(nums) - 1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if s < 0:
                    b += 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                elif s > 0:
                    c -= 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
        return res
