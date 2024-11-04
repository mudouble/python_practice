def integer_sqrt_binary_search(n):
    if n<0:
        return -1
    if n==0 or n==1:
        return n
    low, high = 0,n
    while low<=high:
        mid = (low+high)//2
        if mid*mid == n:
            return mid
        elif mid*mid<n:
            low = mid+1
        else:
            high = mid-1
    return high

def reverse_s(s):
    # stack = []
    # res = ""
    # for item in s.split("."):
    #     stack.append(item)
    # while stack:
    #     res+=stack.pop()+"."
    # print(res[:-1])

    s_list = s.split(".")
    left, right = 0, len(s_list)-1
    while left<right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left+=1
        right-=1
    print(".".join(s_list))

def lcs(strs1, strs2):
    n, m = len(strs1), len(strs2)
    dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if strs1[i-1]==strs2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[n][m])

def compute_prefix_function(pattern):
    next = [0]*len(pattern)
    j=0
    for i in range(1, len(pattern)):
        while j>0 and pattern[i]!=pattern[j]:
            next[i] = j-1
        if pattern[i]==pattern[j]:
            j+=1
        next[i] = j
    return next


def remove_duplicates(code):
    print(code)
    reverse_code = code[::-1]
    print(f"reverse_code: {reverse_code}")
    prefix_length = compute_prefix_function(reverse_code)[-1]
    print(f"prefix_length {prefix_length}")
    total_lines = len(code.split("\n"))
    duplicate_lines = prefix_length//len(code.split("\n")[0])
    if duplicate_lines>=3 and duplicate_lines/total_lines>=0.3:
        truncate_code = reverse_code[prefix_length:]
        return truncate_code[::-1]
    else:
        return code


# KMP算法获取部分匹配表（LPS数组）
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # 前一个最长前缀后缀的长度
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


# 使用KMP算法找到最长前缀
def kmp_longest_prefix_suffix(test):
    reversed_test = test[::-1]  # 翻转字符串
    lps = compute_lps(reversed_test)  # 计算最长前缀
    return lps[-1]  # 返回最长前缀的长度


# 检查并去重超过30%的重复后缀内容
def remove_duplicate_suffix(content):
    # 计算行数
    lines = content.splitlines()
    content_length = len(lines)

    if content_length < 3:  # 长度不足3行，不做处理
        return content

    longest_prefix_len = kmp_longest_prefix_suffix(content)  # 获取去重位置

    # 计算重复内容的字符长度
    # 这里估算出重复行的字符数
    if longest_prefix_len > content_length * 0.3 * len(lines[-1]):
        print(f"Detected {longest_prefix_len} characters to be trimmed as duplicate suffix.")

        # 进行去重
        # 保留去掉重复内容后的完整内容
        trimmed_content = content[:-longest_prefix_len]

        # 确保返回的内容不会包含额外的换行符
        if trimmed_content.endswith('\n'):
            trimmed_content = trimmed_content.rstrip('\n')  # 去除最后的换行符

        return trimmed_content

    return content


# 测试代码
test_code = """
def foo():
    print("Hello")
    print("World")
    print("Hello")
    print("World")
    print("Hello")
    print("World")
"""

clean_code = remove_duplicate_suffix(test_code)
print("去重后的代码:")
print(clean_code)

# if __name__ == '__main__':
#     test_code = """
#     def foo():
#         print("Hello")
#         print("World")
#         print("Hello")
#         print("World")
#         print("Hello")
#         print("World")
#     """
#
#     result = remove_duplicates(test_code)
#     print(result)