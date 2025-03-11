# AWS 客户从世界各地的数据中心引入了服务器和数据库，为其应用程序提供支持。假设所有服务器和数据中心位于一条 一维直线上。

# 你的任务是 优化网络连接。
# 每个数据中心必须连接到一个服务器。

# 给定数据中心的位置数组 center 和服务器目的地的位置数组 destination，其中：

# center[i] 表示数据中心的位置
# destination[i] 表示服务器的位置
# 任意 center[i] 必须 连接到某个 destination[j]，连接的 代价（lag） 定义为 |x - y|（即数据中心 x 和服务器 y 之间的绝对位置差值）。
# 要求：最小化总 lag。

''' 由于 center 和 destination 一一对应，且 |x - y| 计算的是绝对距离，
最优方案是：先对 center 和 destination 排序，再逐一匹配，这样能保证总距离最小。'''

def getMinDistance(center, destination):
    center.sort()
    destination.sort()
    
    total_lag = 0
    for i in range(len(center)):
        total_lag += abs(center[i] - destination[i])
    
    return total_lag

# 示例测试
center = [1, 2, 2]
destination = [5, 2, 4]
print(getMinDistance(center, destination))  # 输出 6
