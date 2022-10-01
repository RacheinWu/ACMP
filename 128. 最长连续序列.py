from typing import List

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         longest_streak = 0
#         nums_set = set(nums)
#         for num in nums_set:
#             if num - 1 not in nums_set:
#                 current_length = 1
#                 current_num = num
#                 while current_num + 1 in nums_set:
#                     current_num += 1
#                     current_length += 1
#                 longest_streak = max(longest_streak, current_length)
#         return longest_streak

#
# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = [x for x in range(n)]
#         self.size = [1 for _ in range(n)]
#         self.part = n
#
#     def Find(self, x: int) -> int:
#         if self.parent[x] == x:
#             return x
#         return self.Find(self.parent[x])
#
#     def Union(self, x: int, y: int) -> bool:
#         root_x = self.Find(x)
#         root_y = self.Find(y)
#         if root_x == root_y:
#             return False
#         if self.size[root_x] > self.size[root_y]:
#             root_x, root_y = root_y, root_x
#         self.parent[root_x] = root_y
#         self.size[root_y] += self.size[root_x]
#         self.part -= 1
#         return True
#
#     """
#         是否在同一个集合中
#     """
#     def is_samepart(self, x: int, y: int) -> bool:
#         return self.Find(x) == self.Find(y)
#
#     """
#         获取一个集合的元素数量
#     """
#     def get_partsize(self, x: int) -> int:
#         root_x = self.Find(x)
#         return self.size[root_x]
#
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#          UF = UnionFind(len(nums))
#          max_length = 0
#
#          for num in nums:
#              if UF.Find(num + 1)
