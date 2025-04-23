# # 4.14 tiktok AI infra mle interview

# # 这道题是经典的“找峰值”（Find Peak Element）问题
# #每次比较 mid 和 mid + 1，如果 mid 比右边大，说明左边存在峰值；
# # 如果 mid 比右边小，说明右边一定有峰值；
# # 最终收敛到一个峰值点。

# # 询问面试官，是不是多个峰值返回一个就可以？互动环节
# # 输入是 0-indexed 数组；
# # 多个峰值返回任意一个即可；
# # 峰值的定义是：比左右两边的数都大；
# # 题目要求 O(log n) 的时间复杂度，O(1) 的空间复杂度；
# 这一题算的上是 easy 级别的题目，面试官给了提示，
# 说是二分查找的思路，直接写代码就可以了。
def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            # 峰值在左边（包括 mid）
            right = mid
        else:
            # 峰值在右边
            left = mid + 1

    return left

# # 示例测试
# print(findPeakElement([1, 2, 3, 1]))         # 输出: 2
# print(findPeakElement([1, 2, 1, 3, 5, 6, 4])) # 输出: 5（或 1，也可以接受）

# 第二题 1000 个灯，编号从 1 到 1000，初始都是灭的。每次操作把编号为 i 的灯打开或关闭。

#一个灯的编号如果有 奇数个因子，那么它最终是亮的；否则是灭的。
# 只有完全平方数才有奇数个因子，我们只需要计算 [1, 1000] 中有多少个 完全平方数
# 这题目虽然短，但实际难度算是medium + 的题目了。
import math

def count_on_off_lights(n):
    # 亮的灯（编号是完全平方数的灯）
    on = int(math.isqrt(n))
    off = n - on
    return on, off

# 示例：1000 个灯
on, off = count_on_off_lights(1000)
#因为 1^2 = 1，2^2 = 4，...，31^2 = 961，32^2 = 1024（超出范围），所以亮灯的就是前 31 个完全平方数
# 最后开着的31个，关的是969个
print(f"Lights ON: {on}, Lights OFF: {off}")

# 题目做完后大约还剩下20分钟，面试官问了一个关于 AI 的问题。
# 你对 AI 的理解是什么？自由回答。

# 面试官可能想深入讨论nlp，cv的内容。技术点
# 比如 q learning，激活函数，loss function，优化算法。
# 问到一些深度学习的框架，比如 pytorch，tensorflow，keras。
# 还有向量数据库，比如graphdb，chormadb, 以及 milvus，faiss，pinecone 等。
# 这些都是 AI 基础知识，面试官会问一些基础概念和原理。