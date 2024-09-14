def func1():
    s = list(input())
    i = len(s) - 1
    while i >= 0:
        if ord("a") <= ord(s[i]) + 1 <= ord("z"):
            s[i] = chr(ord(s[i]) + 1)
            # 容易忘记
            while i + 1 < len(s):
                i += 1
                s[i] = "a"
            return "".join(s)
        i -= 1
    return -1


def func2():
    '''反转两个或者三个数字，多次之后变成有序数组'''
    pass


def func3():
    '''最小化和最大化，两个玩家轮流选择
    零和博弈（一个玩家的得分增加意味着另一个玩家的得分减少）
    '''
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    dp = [[0] * n for i in range(2)]
    for i in range(2):
        for j in range(n):
            if (i + j) % 2 == 0:
                dp[i][j] = max()


def func4():
    n = int(input())
    ans = 0
    for i in range(100, n + 1):
        if i % 100 == 0:
            ans += 1

    print(ans)


def func5():
    n, m, k = map(int, input().split())
    grid = [[0] * (n+1) for _ in range(m+1)]
    for i in range(k):
        s, x, y = input().split()
        x, y = int(x), int(y)
        if x > n or y > m or x <= 0 or y <= 0:
            return -1
        if s == "c":
            grid[x][y] = 1
        elif s=="l":
            flag = 0
            while y-1>=1:
                if grid[x][y-1]==0:
                    flag = 1
                    print(str(x)+" "+str(y-1))
                    break
                y-=1
            if not flag:
                print("-1")
        elif s=="r":
            flag = 0
            while y+1<=m:
                if grid[x][y+1]==0:
                    flag = 1
                    print(str(x)+" "+str(y+1))
                    break
                y+=1
            if not flag:
                print("-1")
        elif s=="u":
            flag = 0
            while x-1>=1:
                if grid[x-1][y]==0:
                    flag=1
                    print(str(x-1)+" "+str(y))
                    break
                x-=1
            if not flag:
                print("-1")
        elif s=="d":
            flag = 0
            while x+1<=n:
                if grid[x+1][y]==0:
                    flag=1
                    print(str(x+1)+" "+str(y))
                    break
                x+=1
            if not flag:
                print("-1")

def func6():
    a, b = map(int, input().split())
    dp = [0]*(b)
    index = 1
    while True:
        dp[index] = dp[index-1]+index
        temp = dp[index]+index+1
        if dp[index]>=a and dp[index]-a == temp-b:
            print(dp[index]-a)
            return dp[index]-a
        index+=1


if __name__ == '__main__':
    # print(func1())
    func6()
