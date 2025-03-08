# def generate_subsequences(s, index=0, current="", result=None):
#     if result is None:
#         result = []
#     if index == len(s):
#         if current:  # 只在 current 非空时才添加到结果中
#             result.append(current)
#         return result
#     # 选择当前字符
#     generate_subsequences(s, index + 1, current + s[index], result)
#     # 不选择当前字符
#     generate_subsequences(s, index + 1, current, result)
#     result.sort()  # 按字母顺序排序
#     return result  # 返回最终的结果列表

def dfs(s,index,current,result):
    if index == len(s):
        if current:
            result.append(current)
        return result
    dfs(s,index+1,current+s[index],result)
    dfs(s,index+1,current,result)
    result.sort()

    return result

# 测试用例
if __name__ == "__main__":
    s = "xyz"
    subsequences = dfs(s,0,"",[])
    print(subsequences)
    # ['x', 'xy', 'xyz', 'xz', 'y', 'yz', 'z']