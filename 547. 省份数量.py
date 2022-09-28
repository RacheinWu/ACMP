from typing import List


class UnionFind:

    def __init__(self):
        """
            记录每个节点的父节点
        """
        self.father = {}
        self.num_of_sets = 0

    def add(self, x):
        # 添加新节点：
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1

    # 两个节点是否连通
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    # # 查找祖先
    # def find(self, x):
    #     root = x
    #     while self.father[root] is not None:
    #         root = self.father[root]
    #     return root

    # 查找祖先 -> 压缩
    def find(self, x):
        root = x

        while self.father[root] is not None:
            root = self.father[root]

        while x is not root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        map_c = UnionFind()  # 创建map
        for i in range(len(isConnected)):
            map_c.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    map_c.merge(i, j)

        return map_c.num_of_sets
