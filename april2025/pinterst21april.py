{
  "boards": [
    {
      "id": "board1",
      "pins": ["pin1", "pin2", "pin3"]
    },
    {
      "id": "board2",
      "pins": ["pin3", "pin4"]
    },
    {
      "id": "board3",
      "pins": ["pin4", "pin5", "pin6"]
    }
  ]
}

from collections import defaultdict
# 构建graph
graph = defaultdict(set)

for board in boards:
    pins = board["pins"]
    for i in range(len(pins)):
        for j in range(i + 1, len(pins)):
            graph[pins[i]].add(pins[j])
            graph[pins[j]].add(pins[i])
from collections import deque

# BFS遍历图，计算每个pin的分数，这个是辅助给的
def bfs_score(start_pin, goal_pin, graph):
    if start_pin == goal_pin:
        return 1.0  # 如果起点和终点相同，分数为1.0
    visited = set()
    queue = deque([(start_pin, 0)])  # (pin, depth)
    score = 0

    while queue:
        pin, depth = queue.popleft()
        if pin in visited:
            continue
        visited.add(pin)
        if pin != start_pin:
# 可以改为 score += 1 / (depth + 1) 以减少远距离影响
# 使用除非的计算分数，可以减少远距离的影响，辅助没有写出来
# 辅助这里还是score += 1，然后计算全局的分数
            score += 1  
        for neighbor in graph[pin]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
    return score
# 面试官不让计算所有pin的分数，不让存储这个。
pin_scores = {}
for pin in graph:
    pin_scores[pin] = bfs_score(pin, graph)


# 只计算pin1到pin2的分数，不需要存储所有pin的分数
# 强调了好多次不要 all pin，辅助一点没听进去，不知道他是不是不懂。
# 面试官要不要存储的方法，应该下面的方法。

# 直接计算pin1到pin2的分数，使用BFS遍历图，计算pin1到pin2的分数
# 这个方法是直接计算pin1到pin2的分数，不需要存储所有pin的分数
def score_by_shortest_path(pin1, pin2, graph):
    from collections import deque
    
    if pin1 == pin2:
        return 1.0
    
    visited = set()
    queue = deque([(pin1, 0)])  # (current_pin, distance)
    
    while queue:
        current, dist = queue.popleft()
        if current == pin2:
            return 1 / (dist + 1)
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
    
    return -1  # 不可达
