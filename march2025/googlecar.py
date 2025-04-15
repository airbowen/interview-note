## google 面试题，车辆分配问题 该问题是3月11 日，谷歌面试题
# 问题描述： 有一批车辆，每辆车有多次出租记录，每次出租记录包括取车时间和还车时间。要求分配车辆，计算最少需要多少辆车。
# 输入：车辆的出租记录列表，每个记录包括取车时间和还车时间  [(pick1, return1), (pick2, return2), ...]
# 输出：最少需要的车辆数    
# leetcode 253. Meeting Rooms II 也是这个问题的变种

# 判断冲突，先给这个list排序，然后判断是否有冲突

def is_conflict(pick1, return1, pick2, return2):
    """判断两个出租记录是否冲突"""
    return not (return1 <= pick2 or return2 <= pick1)

def assign_rentals(rentals: list):
    """分配车辆并存储出租记录，使用字典存储每辆车的记录"""
    rentals.sort()  # 按取车时间排序
    cars = {}  # 使用字典存储车辆的出租记录
    
    for pick, ret in rentals:
        assigned = False
        # 尝试为当前订单分配已有的车
        for car_id, car_rentals in cars.items():
            # 检查车的最后出租记录与新订单是否冲突
            last_pick, last_ret = car_rentals[-1]  # 获取车的最后出租记录
            if not is_conflict(last_pick, last_ret, pick, ret):
                cars[car_id].append((pick, ret))  # 如果没有冲突，分配给该车
                assigned = True
                break
        
        # 如果没有找到合适的车，为新车分配
        if not assigned:
            new_car_id = len(cars) + 1
            cars[new_car_id] = [(pick, ret)]  # 新车分配给新订单

    # 打印每辆车的出租记录
    for car_id, car_rentals in cars.items():
        print(f"车 {car_id} 的出租记录: {car_rentals}")

    return len(cars)  # 返回最少需要的车辆数


# follow up: 如何优化分配算法，使得最少需要的车辆数更少？
# 优化思路：使用最小堆（heapq 模块）来存储车辆的最后归还时间，以便在 O(log n) 的时间内找到最早归还的车辆。
# 堆的时间复杂度为 O(log n)，因为堆最多有 n 个元素。所以总的时间复杂度为 O(n log n)
