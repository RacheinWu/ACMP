class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        def dfs(node):
            # 返回(全关次数，全开次数，子树全关自己开次数，子树全开自己关次数)
            if node is None:
                return (0, 0, 0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 0:
                # 自己是关的
                # 四种选择全关：
                # 1 子树全开，开自己（1），然后全关（2）
                # 2 子树全关
                # 3 下面全关，左右子结点开，开自己（1），然后关（3）
                # 4 下面全开，左右子结点关，切换（3），再切换（2）
                allClose = min(left[1] + right[1] + 2, left[0] + right[0], left[2] + right[2] + 2,
                               left[3] + right[3] + 2)
                # 全开：
                # 1 子树全开，开自己（1）
                # 2 子树全关，全开（2）
                # 3 下面全开，左右子结点关，开（3）
                # 4 下面全关，左右子结点开，开自己（1），切换（3），再切换（2）
                allOpen = min(1 + left[1] + right[1], left[0] + right[0] + 1, left[3] + right[3] + 1,
                              left[2] + right[2] + 3)
                # 子树全关自己开：
                # 1 子树全开，自己关，开（2）
                # 2 子树全关，开（1）
                # 3 下面全关，左右子结点开，开（3）
                # 4 下面全开，左右关，切换（3），（2），（1）
                subOpen = min(left[1] + right[1] + 1, left[0] + right[0] + 1, left[2] + right[2] + 1,
                              left[3] + right[3] + 3)
                # 子树全开自己关：
                # 1 子树全开
                # 2 子树全关，打开自己（1），再切换（2）
                # 3 下面全开，左右子节点关，打开自己（1），再切换（3）
                # 4 下面全关，左右开，切换（3），切换（2）
                subClose = min(left[1] + right[1], left[0] + right[0] + 2, left[3] + right[3] + 2,
                               left[2] + right[2] + 2)
            else:
                # 自己是开的
                # 全关：
                # 1 子树全开，切换（2）；
                # 2 子树全关，切换（1）；
                # 3 下面都关，左右子结点开，切换（3）；
                # 4 下面都开，左右关，自己关（1），切（3），切（2）
                allClose = min(left[1] + right[1] + 1, left[0] + right[0] + 1, left[2] + right[2] + 1,
                               left[3] + right[3] + 3)
                # 全开：
                # 1 子树全开；
                # 2 子树全关，自己关（1），全开（2）；
                # 3 下面都开，左右子结点关，自己关（1），全开（3）；
                # 4 下面都关，左右开，切（3)，切（2）
                allOpen = min(left[1] + right[1], left[0] + right[0] + 2, left[3] + right[3] + 2,
                              left[2] + right[2] + 2)
                # 子树全关自己开：
                # 1 子树全关；
                # 2 子树全开，自己关（1），切换（2）；
                # 3 下面都关，左右子结点开，自己关（1），切换（3）；
                # 4 下面都开，左右关，切（2），切（3）
                subOpen = min(left[0] + right[0], left[1] + right[1] + 2, left[2] + right[2] + 2,
                              left[3] + right[3] + 2)
                # 子树全开自己关：
                # 1 子树全开，关（1）；
                # 2 子树全关，切换（2）；
                # 3 下面都开，左右子结点关，切换（3）；
                # 4 下面都关，左右开，（2）（3）（1）
                subClose = min(left[1] + right[1] + 1, left[0] + right[0] + 1, left[3] + right[3] + 1,
                               left[2] + right[2] + 3)
            return (allClose, allOpen, subOpen, subClose)

        return dfs(root)[0]


作者：philco_z
链接：https: // leetcode.cn / problems / U7WvvU / solution / python3 - by - philco_z - uifb /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。