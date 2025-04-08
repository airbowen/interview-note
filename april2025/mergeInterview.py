# 合并区间，4月6日出现在亚麻面试中，参考链接如下
# https://leetcode.com/problems/merge-intervals/
# https://www.lintcode.com/problem/merge-intervals/description

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        # If merged is empty or there is no overlap, append the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, merge the current interval with the last one in merged
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Test the function with example inputs

if __name__ == "__main__":  
    # Example 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals1))  # Output: [[1,6],[8,10],[15,18]]

    # Example 2
    intervals2 = [[1,4],[4,5]]
    print(merge(intervals2))  # Output: [[1,5]]