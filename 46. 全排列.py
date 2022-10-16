from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def func(cur_nums: List[int], sup_nums: List[int]):
            if not sup_nums:
                res.append(cur_nums)
                print("res=",res)
                return
            for i in range(len(sup_nums)):
                print("*",sup_nums[:i], sup_nums[i+1:])
                func(cur_nums + [sup_nums[i]], sup_nums[:i]+sup_nums[i+1:])
                # cur_nums.pop()
        func(cur_nums=[], sup_nums=nums)
        return res


so = Solution()
print(so.permute(nums=[1, 2, 3]))
