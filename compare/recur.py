#xyz，要求返还xyz 所有的排列，比如，x，xy，xyz，xz，利用到recursion 的解法

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
