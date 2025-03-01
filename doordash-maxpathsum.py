from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> List[int]:
        # 全局变量，记录当前找到的最大路径和
        self.maxSum = float('-inf')
        # 记录最大路径
        self.maxPath = []

        def helper(node: TreeNode) -> Tuple[int, List[int]]:
            if not node:
                return 0, []

            # 递归获取左子树的最大贡献值和路径
            leftSum, leftPath = helper(node.left)
            # 递归获取右子树的最大贡献值和路径
            rightSum, rightPath = helper(node.right)

            # 忽略负数贡献，避免拖累路径
            leftSum = max(0, leftSum)
            rightSum = max(0, rightSum)

            # **计算当前节点为“拐点”时的路径和**
            currentSum = leftSum + rightSum + node.val

            # **更新最大路径和**
            if currentSum > self.maxSum:
                self.maxSum = currentSum
                self.maxPath = leftPath + [node.val] + rightPath  # 更新最大路径

            # 利用python 双返回值的特性，返回给父节点的贡献值和路径
            # **返回给父节点的贡献值**（只能选左或右中的较大者）
            if leftSum > rightSum:
                return leftSum + node.val, leftPath + [node.val]
            else:
                return rightSum + node.val, rightPath + [node.val]

        helper(root)
        #最后只取最大路径列表，不需要返回最大路径和
        return self.maxPath  # 返回路径，而不是最大路径和


# **测试用例**
def test():
    solution = Solution()
    
    # **测试用例 1**: 例题 -10, 9, 20, 15, 7
    root1 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solution.maxPathSum(root1))  # 期望输出: [15, 20, 7]

    # **测试用例 2**: 只有一个节点
    root2 = TreeNode(5)
    print(solution.maxPathSum(root2))  # 期望输出: [5]

    # **测试用例 3**: 只有负数
    root3 = TreeNode(-3)
    print(solution.maxPathSum(root3))  # 期望输出: [-3]

    # **测试用例 4**: 完全二叉树
    root4 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(solution.maxPathSum(root4))  # 期望输出: [2, 1, 3]

    # **测试用例 5**: 复杂树
    root5 = TreeNode(10,
                     TreeNode(2, TreeNode(20), TreeNode(1)),
                     TreeNode(10, None, TreeNode(-25, TreeNode(3), TreeNode(4))))
    print(solution.maxPathSum(root5))  # 期望输出: [20, 2, 10, 10]

test()
