// 这是一个经典的链表题目：反转单链表中从第 m 个节点到第 n 个节点的一段子链表，
// 这题的核心思想是：局部反转链表的子区间 [m, n]，并保持链表其他部分不变。为方便处理头节点变化的情况，我们常常引入一个 dummy 节点（值任意），指向原链表的头节点。这样，即使 m=1，也不用单独处理。
// 就地反转 [m, n] 的节点：
// 设 reverseStart 为第 m 个节点（反转起点）
// 逐个将 m+1 到 n 的节点头插到 prev 后面
#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* reverseBetween(ListNode* head, int m, int n) {

    if (!head || m == n) return head;

    // 创建一个 dummy 节点，便于处理头节点变化$
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* prev = dummy;

    // 将 prev 移动到 m 前一个节点
    for (int i = 1; i < m; ++i) {
        prev = prev->next;
    }

    // reverseStart 是反转区间的起点
    ListNode* reverseStart = prev->next;
    ListNode* curr = reverseStart->next;

    // 在 m 到 n 之间逐个插入到 prev 后面，实现反转
    for (int i = 0; i < n - m; ++i) {
      //你的29行少了，
        reverseStart->next = curr->next;
        curr->next = prev->next;
        prev->next = curr;
        curr = reverseStart->next;
    }
//  不用再res了，直接返还更专业，这个本来就是反转后，新的头节点shij
    return dummy->next;
}
 // null 无需反转，m == n（无需反转）
//head = reverseBetween(nullptr, 1, 1);  
// Output: nullptr（应返回空）
// 你没有写main,
// // 示例测试
int main() {
    // 手动创建链表 1 -> 2 -> 3 -> 4 -> 5
    // ListNode* head = new ListNode(1);
    // head->next = new ListNode(2);
    // head->next->next = new ListNode(3);
    // head->next->next->next = new ListNode(4);
    // head->next->next->next->next = new ListNode(5);
    //使用forloop
    // 用数组初始化链表值
    int values[] = {1, 2, 3, 4, 5};
    int n = sizeof(values) / sizeof(values[0]);

    // 创建链表头结点
    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;

    // 用 for 循环构建剩下的节点
    for (int i = 1; i < n; ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }

    // 测试反转,
    // 面试官说别操心empty了，就全部反转可以了
    // 全部反转 (m == 1 && n == length)
    // m 和 n 越界或非法（实际不合法，需额外判断）
// 虽然题目说 1 ≤ m ≤ n ≤ 长度，但在真实系统中你可能需要判断：

    head = reverseBetween(nullptr, 1, 1);  
    // head = reverseBetween(head, 2, 4);
   

    // 打印链表
    for (ListNode* curr = head; curr != nullptr; curr = curr->next) {
        std::cout << curr->val;
        if (curr->next) std::cout << " -> ";
    }
    std::cout << " -> NULL" << std::endl;

    return 0;
}