# 把数组转换成 set，用于快速判断某个数是否存在。
# 你的10 行，current 少个e 
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # 只有在这个数字是一个序列起点的时候才继续
        if num - 1 not in num_set:
            current_num = num
        # 你的10 行，current 少个e 
            current_streak = 1
# 尽量写的过程中，稍稍解释一下
#只对 序列起点（即 num - 1 不在集合中的 num）进行扩展判断。
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
# 保持一个最大长度的变量。这个动态更新
            longest = max(longest, current_streak)

    return longest

# 示例测试，你直接写
#他没给你输入呢
# 目前的解法的是时间o n更省时间，但是空间o n
#排序 + 线性扫描，  时间复杂度  O(n log n) 空间   O(1)
print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 输出: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))   # 输出: 9
print(longestConsecutive([1,0,1,2]))              # 输出: 3
