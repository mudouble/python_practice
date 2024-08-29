import sys

def connect_graph():
    '''删除边权重值，其实不难，但是理解起来有点困难'''
    T = int(input())
    while T>0:
        T-=1
        n = int(input())
        v = list(map(int, input().split()))
        w = []
        temp = 0
        for i in range(n-1):
            a,b,s = list(map(int, input().split()))
            w.append(s)
            temp+=s
        res = 0
        w.sort()
        w.insert(0, 0)
        for i in range(n):
            temp-=w[i]
            res = max(res, temp+v[i])
        print(res)




def oper():
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        o_times, j_times = [], []
        for item in a:
            if item%2==0:
                o_times.append(item)
            else:
                j_times.append(item)
        flag = 0
        if len(o_times)==0 or n==0:
            count=0
        elif len(j_times)==0:
            for o in o_times:
                if o//2%2!=0:
                    flag = 1
                    break
            if flag==0:
                count = len(o_times)+1
            else:
                count = len(o_times)
        else:
            count = len(o_times)
        print(count)

def judge(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

def exchange():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    max_a, min_a = max(a), min(a)
    sort_a = sorted(a)
    if min_a > x and a!=sort_a:
        ans =-1
    elif min_a>x and a==sort_a:
        ans = 0
    elif max_a>x and a[-1]!=max_a:
        ans = -1
    else:
        while judge(a)==False:
            for i in range(n-1, -1, -1):
                if a[i]<x:
                    a[i], x = x, a[i]
                    ans+=1
                if judge(a):
                    break
            min_a, max_a = min(a), max(a)
            sort_a = sorted(a)
            if min_a > x and a!=sort_a:
                ans=-1
                break
            elif min_a>x and a==sort_a:
                break
            elif max_a>x and a[-1]!=max_a:
                ans = -1
                break
    print(ans)

def turn_around():
    n = int(input())
    a = input()
    ans = 0
    if len(a)<=1:ans = 0
    elif a.count("0")==0:
        ans = 0
    elif a.count("1")==0:
        ans = 0
    elif len(a)%2==0:
        if a.count("0") == a.count("1"):ans = len(a)
        else: ans = min(a.count("0"),a.count("1"))*2
    elif len(a)%2!=0:
        if a.count("0")-1==a.count("1"):
            ans = len(a)
        else:
            ans = min(a.count("0"),a.count("1"))*2
    print(ans)





if __name__ == '__main__':
    connect_graph()




