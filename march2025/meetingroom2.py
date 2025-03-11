# 关连google car 那一题目，这个是leetcode 253. Meeting Rooms II，
import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # 按照会议的开始时间排序
    intervals.sort(key=lambda x: x[0])

    # 最小堆，存储会议的结束时间
    heap = []

    # 将第一个会议的结束时间放入堆中
    heapq.heappush(heap, intervals[0][1])

    # 遍历后续的会议
    for i in intervals[1:]:
        # 如果当前会议的开始时间大于或等于堆顶元素，表示该会议室可以复用
        if heap[0] <= i[0]:
            heapq.heappop(heap)

        # 将当前会议的结束时间加入堆中
        heapq.heappush(heap, i[1])

    # 堆的大小就是最少需要的会议室数
    return len(heap)

# 测试用例 1
intervals_1 = [[0, 30], [5, 10], [15, 20]]
print(f"Test case 1 result: {minMeetingRooms(intervals_1)}")  # 输出 2

# 测试用例 2
intervals_2 = [[7, 10], [2, 4]]
print(f"Test case 2 result: {minMeetingRooms(intervals_2)}")  # 输出 1

# 测试用例 3
intervals_3 = [[1, 5], [8, 9], [8, 9], [4, 6]]
print(f"Test case 3 result: {minMeetingRooms(intervals_3)}")  # 输出 2

# 测试用例 4（没有会议）
intervals_4 = []
print(f"Test case 4 result: {minMeetingRooms(intervals_4)}")  # 输出 0

# 测试用例 5（所有会议都在同一时间）
intervals_5 = [[1, 5], [1, 5], [1, 5]]
print(f"Test case 5 result: {minMeetingRooms(intervals_5)}")  # 输出 3
