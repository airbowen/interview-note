# Given a binary tree, find the maximum path sum from any two "alive nodes" within the tree. 
# We can assume a node is an alive node if and only if it is a leaf node, indicated by an asterisk below.


#      5
#     /  \
#    2    0
#   /    /  \
# *25   *14  *15
# 47 = 25 + 2 + 5 + 15

# 目标是计算叶子节点之间的最大路径和，那么每个**内部节点（非叶子节点）都要以“桥梁”的形式连接两个子树，
# 而不能只返回单侧贡献值。
# 因此，它和 LeetCode 124 题目的解法有本质区别。
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')  # 初始化最大路径和

        def max_subtree_path(root: Optional[TreeNode]) -> int:
            nonlocal max_path  # 允许修改外部变量
            
            if not root:  
                return 0  # 递归终止条件
            
            # 递归计算左右子树的最大路径和
            gain_left = max_subtree_path(root.left)
            gain_right = max_subtree_path(root.right)
            
            # 只有当当前节点是内部节点（左右子树都有），才更新 max_path
            if root.left and root.right:
                max_path = max(max_path, gain_left + gain_right + root.val)
            
            # 递归返回该子树对上层的贡献值（只能选择较大的那一侧）
            return max(gain_left, gain_right) + root.val

        max_subtree_path(root)  # 递归调用
        return max_path  # 返回最终的最大路径和

# Follow - up
# What if any nodes in the tree can be alive instead of just the leaves? 
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float('-inf')

        def max_subtree_path(root: Optional[TreeNode]) -> int:
            if not root:
                return 0  # 空节点返回 0
            
            # 递归计算左右子树的最大贡献值，若贡献值 < 0 则舍弃（取 0）
            gain_left = max(max_subtree_path(root.left), 0)
            gain_right = max(max_subtree_path(root.right), 0)

            # 计算当前子树的最大路径和（root 可能是任意路径的连接点）
            current_sum = gain_left + gain_right + root.val
            self.max_path = max(self.max_path, current_sum)  # 更新最大路径
            
            # 递归返回当前节点对父节点的贡献（只能选一侧）
            return root.val + max(gain_left, gain_right)

        max_subtree_path(root)
        return self.max_path
