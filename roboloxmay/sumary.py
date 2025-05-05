
'''
/// Task Scheduler
'''

每次先取当前剩余次数最多（maxheap）并且可以执行（不在冷却区）的task
当一个task执行后，它不能马上再次执行，需要进入冷却状态 
-> 把它（以及它的剩余次数和恢复可执行的时间点）放入queue


def leastInterval(tasks, n):
    count = Counter(tasks)
    #{'A': 3, 'B': 3, 'C': 2} => [-3, -3, -2]
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0 
    # first in first out
    q = deque() # [[剩余次数，解冻时间]]

    #只要还有待执行任务或冷冻任务
    while maxHeap or q:

        # 如果当前有可执行的任务在maxheap
        if maxHeap: 
            # 取出任务，task剩余次数-1
            cnt = 1 + heapq.heappop(maxHeap)

            # 如果该task还有剩余次数，放入冷冻区
            if cnt !=0:  
                q.append([cnt, time + n]) 

        # 检查冷却队列中是否有任务已冷却完毕
        if q and q[0][1] == time:  
            heapq.heappush(maxHeap, q.popleft()[0])

    return time

Time complexity: O(NlogK) K = 26, N = num of tasks
N个task要处理，每个task要经历heappop/push (logK) 
heapify: O(K)
heap操作: O(logK)

Space complexity: heap(O(K)) + counter(O(K)) + queue(O(K))

====================================

''' 
/// Reorganize String
Given a string s, rearrange the characters of s so that any 
two adjacent characters are not the same. Return any possible 
rearrangement of s or return "" 
if not possible.
'''
每次都优先安排当前剩余次数最多的char,但是不能和当下str的最后一个char相同
用最大堆来存放每个字符及其剩余数量[[-cnt, char]]

def reorganizeString(s):

    ans = []
    # 'aaabbcc' = {'a':3, 'b':2, 'c':2} => [[-3, 'a'], [-2, 'b'], [-2, 'c']]
    maxHeap = [(-count, char) for char, count in Counter(s).items()]
    heapq.heapify(maxHeap)

    #当还有字符没放完
    while maxHeap:

        count_first, char_first = heappop(maxHeap)

        if not ans or char_first != ans[-1]:
            ans.append(char_first)
            #如果该char没用完，讲其次数-1再放回maxheap
            if count_first + 1 != 0: 
                heappush(maxHeap, (count_first + 1, char_first))

        #如果count_first和str尾部字符相同，需要找第二频繁的字符来追加
        else:
            # 先检查maxheap是否还有char,如果没有了，返回‘’
            if not maxHeap: return ''
            count_second, char_second = heappop(maxHeap)

            ans.append(char_second)

            if count_second + 1 != 0:
                heappush(maxHeap, (count_second + 1, char_second))

            # 把之前无法放置的第一个字符 (char_first) 原封不动地放回堆里
            # 因此这次没有使用，所以count不应该减少   
            heappush(maxHeap, (count_first, char_first))


    return ''.join(ans)

Time complextiy: O(NlogK) K = 26, N = num of char
N个char要处理，每个char要经历heappop/push (logK) 
Counter: O(N)
heapify: O(K)

Space complexity: ans (O(N)) + heap(O(K)) + counter(O(K))

====================================

'''
/// Maximize distance to closest person

'''
1001010
从左到右遍历array，记录人左侧最近的1，最后算这个人到末尾的距离

def maxDistToClosest(seats):

    # 左侧最近的1的位置
    prev_seat = None
    #初始化最大距离为-inf
    dist = float('-inf')

    for idx in range(len(seats)):

        if seats[idx] == 1:
            # 左侧没有1，这是他第一次遇到人
            if prev_seat == None: 
                dist = idx
            # 左侧有1，他在两个人中间
            else:
                dist = max(dist, (idx - prev_seat) //2)
            # 更新左侧最近的1为他当下位置
            prev_seat = idx

    # 单独处理最后一个人到末尾的距离
    dist = max(dist, len(seats) -1 - prev_seat)
    return dist



Time Complexity: O(n)
Space Complexity: O(1)


===============================================

'''
/// Remove prefix strings in a list of string.

Example 1: input {"a", "ab", "abc"} -> output: {"abc"}.
Example 2: input {"a", "bc", "ab", "abc hello"} --> output: {"bc", "abc hello"}.

要求： output array 要保持String 在input 里的顺序。
'''
我们用一个trie来存放所有word
针对每个word，在trie中沿着它的每个char走，如果到end时发现下面还有childnode，
则它是其他word的前缀，要抛弃它。

我们用一个 嵌套的 dict 来模拟 Trie，每个节点是一个 dict。
{
  'a': {'b': {'#': True}},
  'x': {'y': {'z': {'#': True}}}
}

def removePrefixStrings(words):
    trie = {}  # 用 dict 模拟 Trie
    # 插入 word 如 "abcda" 到 trie
    def insert(word):
        # 从根节点开始
        node = trie
        
        for c in word:
            # 如果字符 c 不是当前节点的子节点 (key)
            if c not in node: 
                # 给c在trie中创建一个新的node (空字典)
                node[c] = {} 
            # 进入c的childnode
            node = node[c] 

        # word遍历结束后，在当前节点标记单词结束
        node['#'] = True  

    # 判断当前单词是否是其他单词的前缀
    def is_prefix_of_other(word, trie):
        # 从根节点开始
        node = trie
        # 我们沿着这个单词 word 一步一步往下走；
        for c in word:

            # 如果字母c不在当前的node的key里
            # 说明这个trie的开头前len(word)个字母里有和word不一致的
            if c not in node:
                return False
            # 沿着word往下走    
            node = node[c]

        # 如果当前node的所有key(childnode)中有不是‘#’的
        return any(k != '#' for k in node)

    # 构建 Trie
    for word in words:
        insert(word)

    # 保留不是其他字符串前缀的词，按原始顺序输出
    return [word for word in words if not is_prefix_of_other(word, trie)]


Time complexity: O(S)
S = len(words)*num_words
Trie: O(S)
check all words: O(S)

Space complexity: O(S) 最差情况，trie里存了独立的每个word

====================================

'''
A trie (pronounced as "try") or prefix tree is a tree data structure 
used to efficiently store and retrieve keys in a dataset of strings. 

insert(word) Inserts the string word into the trie.
search(word) Returns true if the string word is in the trie (i.e., was inserted before)
startswith(prefix): Returns true if there is a previously inserted string word 
that has the prefix prefix

Implement the Trie class:

Trie() Initializes the trie object.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root # start from root
        for char in word:
            # 如果char不在当前node的children里，就加入char
            if char not in node.children:
                node.children[char] = TrieNode()

            # 向下延伸到node 的child
            node = node.children[char]

        # 遍历完整个word，把每个char插入到trie中后，令is_end = true    
        node.is_end = True

    def search(word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(prefix):
        node = self._find_node(prefix)
        return node is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

## 
# len(word) = m

## Time complexity
# insert: O(m) 遍历word每个单词
# search: O(m) 逐个char查找是否存在
# startswith: O(m)

## Space complexity
## insert: O(m)
# search: O(1)
# startswith: O(1)



=============================================



''' /// Is the function Valid
第一问
写一道判断func是不是输入完成的函数叫isFuncComplete，比如
print( -> false
print() -> true
输入一个string，返回bool，不需要判断太复杂的逻辑，面试官其实只需要判断括号是不是对齐了

第二问
括号种类升级到了（【{，需要进行上面的类似判断

第三问
额外增加了引号，判断是否输入完成
'''

## 只解决括号
def isFuncComplete(s):
    count = 0
    for c in s:
        if c == '(': count += 1
        if c == ')': 
            count -= 1
            # if more ) than (, then there must be a false ())
            if count < 0: return False
    return count == 0


## 第三问
def isFuncComplete(s: str) -> bool:

    # we could use stack, first in first out
    stack = []
    closeToOpen = {')': '(', ']': '[', '}': '{'}
    quote = None

    for c in s:
        # check if there are single quote or pair of quote
        if c in ("'", '"'):
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            continue

        # don't get it
        if quote:
            continue  # 跳过引号内字符

        if c in closeToOpen:
            # why if stack in front ?
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False

        elif c in closeToOpen.values():

            stack.append(c)

    return not stack and quote is None



Time complexity : O(n)
Space complexity: O(n)


====================================

''' /// Valid Parenthesis
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''

def isValid(s):
    stack = []
    closeToOpen = {')':'(', ']':'[', '}':'{'}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False



====================================

'''
/// Rotate the box
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

'''

def rotateBox(box):

    m, n = len(box), len(box[0])

    # Traverse each row
    for row in box:
        # the right most position could move the stone to
        write = n - 1  
        for j in range(n - 1, -1, -1):
            if row[j] == '*':
                write = j - 1  # move write to the left
            elif row[j] == '#':
                row[j] = '.'  # remove stone from original position
                row[write] = '#'  # move stone to the lowest possible position
                write -= 1

    # Rotate the box 90 degrees clockwise
    rotated = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated[j][m - 1 - i] = box[i][j] # m - 1 - i is the number of rows to the bottom of rotated box

    return rotated



Time complexity: O(m*n)
Space complexity: O(m*n)


=========================================

''' 
/// ID Pool
让实现一个ID pool，ID的range是1到max long。有俩API acquire（）和release（），
前者返回一个最小的空闲的id，后者收回一个正在使用的ID，把它重新放回池子。

'''

import heapq

class IDPool:

    # 优先从 released 中拿最小的 ID
    # 若没有释放的 ID 可用，再从 next_id 开始分配新 ID
    # 每个 ID 最多只在一个地方出现（used、released、或 next_id 尚未发出）

    def __init__(self):

        self.next_id = 1  # 从未用过的id
        # 用户曾经 acquire 后又 release 回来 的 ID （用minheap存）
        self.released = [] 
        self.used = set() # 记录当前正在使用的 id

    # 返回最小空闲的id
    def acquire(self)：

        if self.released: #如果minheap不为空，那就把top元素pop
            # 取最小的空闲 ID
            id = heapq.heappop(self.released)

        else:
            id = self.next_id
            self.next_id += 1

        self.used.add(id)

        return id

    # 收回一个正在使用的id，并重新放回pool
    def release(self, id):
        if id in self.used:
            self.used.remove(id)
            heapq.heappush(self.released, id)





========================================

'''
/// Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

'''

这个技巧来自滑动窗口思想。

AtMost(k)：表示子数组中最多有 k 个不同整数的子数组个数
AtMost(k-1)：表示子数组中最多有 k-1 个不同整数的子数组个数
二者相减，就是“正好有 k 个不同整数”的子数组个数

我们用滑动窗口从左到右遍历一遍array,
每次往右边加一个新数字，看看它是不是distinct
如果窗口里不同数字超过k个，那我么就从左边删一些，知道窗口里数字不超过k个
每次窗口合法，我们就能数出以当前右边界结尾的子数组数量

from collections import defaultdict


def subarraysWithKDistinct(nums, k):
    # 内部函数：返回最多有 k 个不同整数的子数组数
    def atMostK(nums, k):
        count = defaultdict(int)  # 存每个整数的出现次数
        left = 0                 # 滑动窗口的左边界
        result = 0               # 最终答案

        # 遍历每个右边界
        for right in range(len(nums)):
            # 如果 nums[right] 是新数字，减少k
            if count[nums[right]] == 0:
                k -= 1
            # 把 nums[right] 加进当前窗口
            count[nums[right]] += 1

            # 如果不同整数超过 k，左边收缩窗口
            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1  # 去掉一个不同的整数
                left += 1  # 左边界右移

            # 所有以 right 为右边界的子数组中，合法的是 [left, right] 范围内的子数组
            result += right - left + 1

        return result

    # 利用公式：Exactly(k) = AtMost(k) - AtMost(k-1)
    return atMostK(nums, k) - atMostK(nums, k - 1)




=======================================

'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it can trap 
after raining.

'''

对于数组中的每一个位置，能存储的水量取决于它左边和右边最高的柱子。
当前位置能存储的水量等于其左右两边最高柱子中的较小者减去当前位置的高度。

我们可以使用动态规划的思想，预先计算每个位置左边和右边的最高柱子高度，
然后再计算每个位置能存储的水量。



def trap(height):

    n = len(height)
    if n == 0:
        return 0

    # 初始化一个和height等长度的数组left_max, 存放height每个位置的左边最大高度
    left_max = [0] * n
    left_max[0] = height[0]

    for i in range(1, n):
        # 当前左边最大高度为前一个位置的左边最大高度和当前高度的较大者
        left_max[i] = max(left_max[i - 1], height[i])

    # 初始化右边最大高度数组
    right_max = [0] * n
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        # 当前右边最大高度为后一个位置的右边最大高度和当前高度的较大者
        right_max[i] = max(right_max[i + 1], height[i])

    # 计算总的存水量
    water = 0
    for i in range(n):
        # 当前能存的水为左右最大高度的较小者减去当前高度
        water += min(left_max[i], right_max[i]) - height[i]

    return water


Time complexity: O(n)
Space complexity: O(n)

=======================================

'''
Number of Adjacent elements with the same color

You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

Set colors[indexi] to colori.
Count adjacent pairs in colors set to the same color (regardless of colori).
Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

Output: [0,1,1,0,2]

'''

你有一个长度为 n 的数组 colors，初始时所有元素都是 0，表示未上色。
你会收到一系列的上色请求 queries，每个请求是 [index, color]，
表示将 colors[index] 设置为 color。
每处理一个请求后，你需要统计数组中有多少对相邻的元素颜色相同（且不为 0）。


关键点：
每次只需要关注被修改位置的左右相邻元素。
如果修改前后相邻元素的颜色发生变化，可能会增加或减少相同颜色的相邻对数。


def colorTheArray(n, queries):

    # 初始化颜色数组
    colors = [0] * n  
    # 存放每次查询结果
    result = []       
    # 当前相同颜色的相邻对数
    count = 0         

    # 判断 index 和邻居是否是有效的相邻对
    def adjacent_pair(index):
        pair = 0
        if index > 0 and colors[index] == colors[index - 1]:
            pair += 1
        if index < n - 1 and colors[index] == colors[index + 1]:
            pair += 1
        return pair

    for index, color in queries:
        # 只要没上过色的位置，color才会是0
        if colors[index] != 0:
            # 删除旧颜色带来的相邻对（如果有）
            count -= adjacent_pair(index)
        
        colors[index] = color  # 更新颜色

        # 添加新颜色带来的相邻对（如果有）
        count += adjacent_pair(index)

        result.append(count)

    return result


