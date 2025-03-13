from heapq import heappop, heappush, heapify
from collections import Counter

# 第一问：重排字符串    yama intern 1st question
# 给定一个字符串，要求重新排列字符串，使得相邻字符不相同
def rearrange_string(s):
    # 统计字符出现的次数
    counter = Counter(s)
    # 使用最大堆存储字符，按照频率排序（使用负数模拟最大堆）
    max_heap = [(-freq, char) for char, freq in counter.items()]
    heapify(max_heap)
    
    result = []
    prev_freq, prev_char = 0, ''
    
    while max_heap:
        freq, char = heappop(max_heap)  # 取出最高频的字符
        result.append(char)
        
        # 如果前一个字符仍有剩余，则重新放回堆中
        if prev_freq < 0:
            heappush(max_heap, (prev_freq, prev_char))
        
        # 更新 prev_freq 和 prev_char
        prev_freq, prev_char = freq + 1, char  # 频率减1
    
    # 如果结果长度不等于原字符串长度，则说明无法满足条件
    return "".join(result) if len(result) == len(s) else ""

# 测试
print(rearrange_string("bcaab"))  # 可能输出 "abacb"
print(rearrange_string("aaabbc"))  # 可能输出 "ababac"
print(rearrange_string("aaa"))  # 无法重新排列，返回 ""

# 第二问 yama intern 2nd question

# 还是hashset ，两数之和那种
def find_pairs(nums, target):
    seen = set()
    pairs = []
    
    for num in set(nums):
        complement = target - num  # 计算当前数需要的匹配值
        if complement in seen:
            pairs.append((num, complement))  # 形成数对
        seen.add(num)  # 记录当前数
    
    return set(pairs)

# 测试
nums = [1, 3, 6, 2, 3, 4]
target = 5
print(find_pairs(nums, target))  # 可能输出: [(3, 2), (4, 1)]