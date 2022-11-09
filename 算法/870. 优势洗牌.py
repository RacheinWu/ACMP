from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 贪心
        n = len(nums1)
        ans = [0] * n
        nums1.sort()
        ids = sorted(range(n), key=lambda i: nums2[i])
        print(ids)
        # left, right = 0, n-1
        # for x in nums1:
        #     if x > nums2[ids[left]]:
        #         ans[ids[left]] = x
        #         left += 1


so = Solution()
so.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11])