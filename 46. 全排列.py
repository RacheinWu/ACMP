from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_list: List[int], sur_list: List[int]):
            """
            :param cur_list: 当前数组
            :param p: 剩余数字的开头下表

            """
            # 递归终止条件 -> 当p = len(nums) 的时候
            if not sur_list:
                res.append(cur_list)
                return
            for i in range(len(sur_list)):
                dfs(cur_list + [sur_list[i]], (sur_list[:i] + sur_list[i+1:]))

        dfs([], nums)
        return res


so = Solution()
so.permute(nums = [1])
