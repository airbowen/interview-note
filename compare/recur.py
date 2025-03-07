#xyz，要求返还xyz 所有的排列，比如，x，xy，xyz，xz，利用到recursion 的解法

# 这个写法 不需要使用 pop()，因为 current 变量是 字符串（immutable，不可变对象），每次递归调用时，Python 会创建一个新的字符串实例，而不会修改原来的 current。

# 如果是 列表（list），比如 current = []，那就需要 pop()，因为列表是 可变对象，递归回溯时要手动撤销状态，避免影响其他分支。

# current + s[index] 生成了 一个新的字符串，并没有修改 current 本身，所以不会影响其他递归分支。

def generate_subsequences(s, index=0, current="", result=None):
    if result is None:
        result = []
    if index == len(s):
        result.append(current)  # 终止条件时存储当前子序列
        return result
    # 选择当前字符
    generate_subsequences(s, index + 1, current + s[index], result)
    # 不选择当前字符
    generate_subsequences(s, index + 1, current, result)
    return result  # 返回最终的结果列表

# 调用函数
subsequences = generate_subsequences("xyz")
print(subsequences)
# ['xyz', 'xy', 'xz', 'x', 'yz', 'y', 'z', '']

# 与之类似的，还有leetcode 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        
        def dfs(i: int) -> None:
            if i == n:  # 子集构造完毕
                ans.append(path.copy())  # 复制 path，也可以写 path[:]
                return
                
            # 不选 nums[i]
            dfs(i + 1)
            
            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()  # 恢复现场
            
        dfs(0)
        return ans
