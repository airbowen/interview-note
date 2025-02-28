# doordash 热门题目 menu diff 
"""
At DoorDash, menus are updated daily even hourly to keep them up-to-date. 
Each menu can be regarded as a tree. A menu can have many categories; 
each category can have many menu_items; each menu_item can have many item_extras; 
An item_extra can have many item_extra_options…
We will compare the new menu sent from the merchant with our existing menu.
Each item can be considered as a node in the tree. The definition of a node is defined above. 
Either value change or the active status change means the node has been changed. 
There are times when the new menu tree structure is different from existing trees,
which means some nodes are set to null. 
In this case, we only do soft delete for any nodes in the menu.
If that node or its sub-children are null, we will treat them ALL as inactive.

There are no duplicate nodes with the same key. (这是重点： 需要一个active flag来标记节点是否被删除，因为之前的节点可能被删除了，但是新的节点没有被添加。)
Return the number of changed nodes in the tree. （这也是重点，要查找的是多少node 被修改了）
"""

#       Existing tree                                                   
#         a(1, T)                                                 
#       /         \                                                 
#     b(2, T)   c(3, T)                                   
#   /       \           \                                          
# d(4, T) e(5, T)      g(7, T)                       

#             New tree
#             a(1, T)
#           /        \                                             
#    b(2, T)         c(3, T)  
#    /    |    \           \    
# d(4, T) e(5, T) f(6, T)    g(7, F) 

# 它涉及以下几个方面的考察点：

# 树的遍历（Tree Traversal）
# 代码使用递归方式遍历两棵树，比较它们的结构和节点内容的变化。
# 由于每个节点可能有多个子节点，因此这是通用树（General Tree），而不是二叉树（Binary Tree）。

# 差异检测（Diffing Algorithm）
# 代码对比两棵树，判断新增、删除和修改的节点数量，类似于 Git diff 计算代码变更的方法。
# 这种算法常用于 菜单变更、配置更新、版本管理 等场景。
# 哈希映射优化（Hash Map Optimization）

# 代码使用 字典（HashMap） 存储子节点，避免了 O(n²) 复杂度的嵌套循环搜索，提高了查找速度（O(1) 查找子节点）。
# 递归思想（Recursion）

# 软删除（Soft Delete）
# 识别删除、添加、修改的内容
# 计算变更的影响范围
# 递归遍历树结构查找变化

class Node:
    def __init__(self, key, value, is_active):
        self.key = key            # 节点的键
        self.value = value        # 节点的值
        self.is_active = is_active  # 节点的活动状态
        self.children = []        # 子节点列表


def get_modified_items(old_menu, new_menu):
    """ 递归比较旧菜单和新菜单的节点，并计算变化的数量 """
    if old_menu is None and new_menu is None:
        return 0
    
    count = 0

    # 如果一个节点存在而另一个不存在，或者两个节点的 key/value 不同，计数增加
    if old_menu is None or new_menu is None or (old_menu.key != new_menu.key or old_menu.value != new_menu.value):
        #print(f'Changed Node: {old_menu} -> {new_menu}')
        count += 1

    # 获取子节点字典
    children_old = get_child_nodes(old_menu)
    children_new = get_child_nodes(new_menu)

    # 遍历旧菜单中的每个子节点
    for key in children_old:
        count += get_modified_items(children_old[key], children_new.get(key))

    # 检查新菜单中存在但旧菜单中没有的节点
    for key in children_new:
        if key not in children_old:
            count += get_modified_items(None, children_new[key])

    return count


def get_child_nodes(menu):
    """ 返回节点的子节点字典 """
    children_map = {}
    if menu is None:
        return children_map

    for child in menu.children:
        children_map[child.key] = child
    return children_map


# 示例输入
if __name__ == "__main__":
    # 创建旧菜单树
    a = Node('a', 1, True)
    b = Node('b', 2, True)
    c = Node('c', 3, True)
    d = Node('d', 4, True)
    e = Node('e', 5, True)

    a.children = [b, c]
    b.children = [d, e]

    # 创建新菜单树
    a1 = Node('a', 1, True)
    b1 = Node('b', 2, True)
    c1 = Node('c', 3, False)  # 活动状态变化 (不计数)
    d1 = Node('d', 4, True)
    e1 = Node('e', 5, True)
    f1 = Node('f', 6, True)    # 新增节点

    a1.children = [b1, c1]
    b1.children = [d1]  # e1 被移除
    c1.children = [e1]  # e1 变成 c1 的子节点

    # 计算并输出变化的节点数量
    count = get_modified_items(a, a1)
    print(f'Changed Items are: {count}')


# 类似问题 LeetCode 543: Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

#类似问题 LeetCode 543: Diameter of Binary Tree
# Example usage:
# Constructing the binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            l_len = dfs(node.left) + 1  # 左子树最大链长+1
            r_len = dfs(node.right) + 1  # 右子树最大链长+1
            nonlocal ans
            ans = max(ans, l_len + r_len)  # 两条链拼成路径
            return max(l_len, r_len)  # 当前子树最大链长
        dfs(root)
        return ans
    
# 类似问题 LeetCode 124: Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0  # 没有节点，和为 0
            l_val = dfs(node.left)  # 左子树最大链和
            r_val = dfs(node.right)  # 右子树最大链和
            nonlocal ans
            ans = max(ans, l_val + r_val + node.val)  # 两条链拼成路径
            return max(max(l_val, r_val) + node.val, 0)  # 当前子树最大链和（注意这里和 0 取最大值了）
        dfs(root)
        return ans
