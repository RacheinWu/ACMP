from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []
        n = len(nums)
        for i in range(0, n):
            tmp.append(nums[i])
            for j in range(i+1, n):
                tmp.append(nums[j])
                for k in range(j+1, n):
                    tmp.append(nums[k])
                    if sum(tmp) != 0:
                        tmp.pop()
                        continue
                    result.append(tmp.copy())
                    tmp.pop()
                tmp.pop()
            tmp.pop()

        return result
