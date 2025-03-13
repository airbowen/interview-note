from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val  # 定义节点的比较方式，使其可放入最小堆

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    
    # 1. 将所有链表的头节点加入最小堆
    for node in lists:
        if node:
            heappush(heap, node)
    
    dummy = ListNode(0)
    curr = dummy
    
    # 2. 每次取出堆中最小的元素，并将其 next 节点加入堆
    while heap:
        node = heappop(heap)  # 取出最小值节点
        curr.next = node
        curr = curr.next
        if node.next:
            heappush(heap, node.next)  # 插入下一个节点
    
    return dummy.next  # 返回合并后的链表
