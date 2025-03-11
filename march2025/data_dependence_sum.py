
import math
import time
# A 的数据分析师正在分析时间序列数据。他们发现，第 n 个数据项依赖于某个第 x 天的数据，当且仅当存在一个正整数 k，满足：

# floor(n/k)=x
# 其中 floor(z) 表示 z 向下取整后的最大整数。

# 要求： 给定 n，求出所有依赖的 x 值的总和。

# 第一个版本的函数
def getDataDependenceSum_v1(n):
    unique_x_values = set()
    for k in range(1, n + 1):
        x = n // k
        unique_x_values.add(x)
    return sum(unique_x_values)

# 第二个版本的函数
def getDataDependenceSum_v2(n):
    total_sum = 0
    for x in range(n + 1):
        k = n // x if x > 0 else n + 1  # Prevent division by zero
        if k > 0 and math.floor(n / k) == x:
            total_sum += x
    return total_sum

if __name__ == "__main__":
    n = 10000  # 可以调整测试的范围

    # 记录第一个版本的执行时间
    start_time_v1 = time.time()
    result_v1 = getDataDependenceSum_v1(n)
    end_time_v1 = time.time()

    # 记录第二个版本的执行时间
    start_time_v2 = time.time()
    result_v2 = getDataDependenceSum_v2(n)
    end_time_v2 = time.time()

    # 输出测试结果
    execution_time_v1 = end_time_v1 - start_time_v1
    execution_time_v2 = end_time_v2 - start_time_v2

    print(f"Version 1 Result: {result_v1}, Execution Time: {execution_time_v1}")
    print(f"Version 2 Result: {result_v2}, Execution Time: {execution_time_v2}")
