import math
from collections import defaultdict
from time import time


def fun1():
    '''已知x+y和xy求x和y的n次方和'''
    n = 3
    xy = 1
    x_plus_y = 2
    s0 = 2
    s1 = x_plus_y
    for i in range(2, n+1):
        s = x_plus_y*s1 - xy*s0
        s0 = s1
        s1 = s
    print(s)
    
def func2():
    '''有n个数，求可以构造多少个不同的二叉搜索树
    等于左右子树的乘积，对于根节点i，左子树有i-1个节点可以构成二叉搜索树，右子树有n-i个节点构成二叉搜索树
    dp[i]表示i个节点的二叉搜索树个数
    '''
    n = 3
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i]+=dp[j-1]*dp[i-j]
    return dp[n]

def func3():
    '''操作最优化，从a变成b操作的最少次数'''
    a, b = "010101", "101010"
    if len(a)!=len(b):return
    diff = sum(1 for x, y in zip(a,b) if x!=y)
    if diff%2!=0:
        no_flip_operations = (diff-1)//2+1
    else:
        no_flip_operations = diff//2
    
    a_reverse = a[::-1]
    diff_reverse = sum(1 for x,y in zip(a, b)if x!=y)
    if diff_reverse % 2 !=0:
        flip_operations =  (diff_reverse-1)//2+1
    else:
        flip_operations = diff_reverse//2+1

    print(min(no_flip_operations, flip_operations))
        
def func4():
    '''给字符串s，辅音不能相邻，求最大能组成的字符串长度
    dp[i]表示当前字符能组成的最长子串
    '''
    s = "abacabadabacaba"
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    n = len(s)
    dp = [1]*n
    last_vowels = -1
    for i in range(n):
        if s[i] in vowels:
            dp[i] = dp[i-1]+1 if i>0 else 1
            last_vowels = i
        elif s[i] in consonants:
            if last_vowels!=-1:
                dp[i] = dp[last_vowels]+1
            else:
                dp[i] = 1
    print(max(dp))

def func4_1():
    s = "abacabadabacaba"
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    
    def backtracing(index, currwent_length):
        nonlocal max_length
        if index==len(s):
            max_length = max(max_length, currwent_length)
            return 
        if s[index] in vowels:
            backtracing(index+1, currwent_length+1)
        if s[index] in consonants:
            if currwent_length ==0 or s[index-1] in vowels:
                backtracing(index+1, currwent_length+1)
        if currwent_length+len(s)-index<=max_length:
            return 

    max_length = 0
    backtracing(0, 0)
    print(max_length)

def func5():
    '''编辑距离
    dp[i][j]表示word1的前i个字符转换为word2的前j个字符的最少操作
    初始化 dp[i][0]表示将word1的前i个字符转为空字符的操作数，i次删除
          dp[0][j]表示将空字符转换word2的前j个字符，j次插入
        
    转移方程：对于每对字符(i,j)
        如果word1[i-1]==word2[j-1], dp[i][j] = dp[i-1][j-1]
        否则：
            插入操作：dp[i][j] = dp[i][j-1]+1  在word1的末尾插入word2[j-1]
            删除操作：dp[i][j] = dp[i-1][j]+1 删除word1[i-1]
            替换操作：dp[i][j] = dp[i-1][j-1]+1 将word1[i-1]替换为word[j-1]
            取最小
    dp[m][n]将word1转换为word2的最少操作次数
    '''
    word1, word2 = "intention", "execution"
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1
                )
    print(dp[m][n])

def func6():
    s = input().split(",")
    nums = []
    max_num, max_index, min_num = 0, 0, math.inf
    for i in range(len(s)):
        ch = s[i]
        a, b = map(int, ch.split(":"))
        nums.append([a, b])
        if b > max_num:
            max_index = i
            max_num = b
        if b<min_num:
            min_num = b
    if min_num > 4800:return -1
    res = max_num
    for i in range(max_index):
        res += nums[i][0]
    temp = 0
    for i in range(max_index+1,  len(nums)):
        temp+=nums[i][0]
        
    if temp>max_num-nums[max_index][0]:
        res+=temp-(max_num-nums[max_index][0])
    if res>4800:
        return -1
    else:
        return res


def minInsertions(s: str) -> int:
    '''
    没有考虑到的点：栈空或者不匹配都需要插入，
    '''
    stack = []
    insertions = 0

    for char in s:
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']' or char == ')':
            if not stack:
                # No matching opening bracket, need to insert one
                insertions += 1
            else:
                top = stack.pop()
                if (char == ']' and top != '[') or (char == ')' and top != '('):
                    # Mismatched brackets, need to insert one
                    insertions += 1

    # For any unmatched opening brackets left in the stack
    insertions += len(stack)

    return insertions

def func7(n, edges):
    '''图的染色'''
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    colors = [-1]*(n+1)

    def dfs(node, parent_color):
        current_color = 1-parent_color
        colors[node] = current_color
        for neighbor in tree[node]:
            if colors[neighbor] == -1:
                dfs(neighbor, current_color)
    dfs(1, 1)
    return colors[1:]

def func8():
    a_list = list(map(int, input().split()))
    b = []
    res = []
    for i in range(len(a_list)):
        if a_list[i] not in b:
            b.append(a_list[i])
        else:
            index = b.index(a_list[i])
            res.extend(b[index:][::-1])
            b = b[:index]
            b.append(a_list[i])
    print(b)
    res.extend(b[::-1])
    print(res)
    return res

def func9():
    t = time()
    n = int(input())
    nums = list(map(int, input().split()))
    interval = int(input())
    nums.sort()
    res = 0
    for i in range(n):
        temp = nums[i]
        k = nums.count(nums[i])
        while temp+interval<=max(nums):
            temp += interval

            if temp in nums:
                k+=1
        if k > res:
            res = k
            ans = nums[i]
    print(res, ans)
    t1 = time()
    print(t1-t)
    
def func9_1():
    n = int(input())
    nums = list(map(int, input().split()))
    interval = int(input())
    d = defaultdict()
    res,ans = 0, -1
    nums.sort()
    for num in nums:
        if num%interval in nums:
            d[num%interval] += 1
            if d[num%interval]>res:
                res = num%interval
                ans = num
    print(d)
    print(res, ans)
    
def func10():
    n, k = map(int, input().split())
    schedule = []
    for i in range(n):
        schedule.append(list(map(int, input().split())))
    schedule.sort(key=lambda x:(x[0], x[1]))
    print(schedule)
    res = 0
    day = 1
    temp = k
    for item in schedule:
        start, end = item[0], item[1]
        # 如果当前的day小于活动的起点，则更新day为活动的起点
        if day<start:
            day = start
            temp = k
        # 如果当前day在活动区间内，且当天还能参加活动
        if start<=day<=end and temp>0:
            print(item)
            res+=1
            temp-=1
            if temp==0:
                day+=1
                temp = k

    print(res, day)
            
        
        
        





if __name__ == '__main__':
    # Example usage
    func10()
''''
3 1
1 2
2 3
1 1
'''