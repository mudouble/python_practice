import copy
import math
from collections import defaultdict


def gambling():
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    X.sort()
    Y.sort()
    index_x, index_y = 0, 0
    ans = 0
    while index_x < len(X) and index_y < len(Y):
        if X[index_x] > Y[index_y]:
            ans += 1
            index_x += 1
            index_y += 1
        elif X[index_x] <= Y[index_y]:
            index_x += 1
    print(ans)
    return ans

def ok(x, n, price, k):
    now = price[0]+x
    for i in range(1, n):
        if price[i]*1.0/now>k/100.0:return False
        now+=price[i]
    return True
def stock():
    t = int(input())
    for i in range(t):
        n, k = int(input().split())
        price = list(map(int, input().split()))
        l=0
        r=1e9
        ans =0
        while l<=r:
           mid = (l+r)//2
           if(ok(mid)):
                r =mid-1
                ans = mid
           else:l=mid+1
        print(ans)

def edit_distance():
    t = int(input())
    for i in range(t):
        m = int(input())
        s = input()
        ans = 0
        count_pd = s.count("PD")
        if count_pd>0 and m>0:
            s = s.replace("PD", "")
            if m>=count_pd:
                ans += count_pd
                m -= count_pd
            else:
                ans += m
                m = 0
        count_dd = s.count("DD")
        if m >0 and count_dd>0:
            s = s.replace("DD", "")
            if m>=count_dd:
                ans += count_dd
                m-=count_dd
            else:
                ans += m
                m=0
        count_p = s.count("P")
        if m>0 and count_p>0:
            s = s.replace("P", "")
            if m>=count_p:
                ans += count_p
                m-=count_p * 2
            else:
                ans +=m
                m=0
        count_d = s.count("D")
        if m>0 and count_d>0:
            s = s.replace("D", "")
            if m>=count_d:
                ans += count_d
                m-=count_d * 2
            else:
                ans+=m
                m = 0
        while m>=3:
            ans+=1
            m-=3

        print(ans)

def build_defend():
    T = int(input())
    for i in range(T):
        n, t = list(map(int, input().split()))
        times = list(map(int, input().split()))
        count=0
        for i in range(n-1):
            if t>=times[i]:
                t-=times[i]
                if t<times[i+1]:
                    count+=1
        print(count+1)

def count_num():
    T = int(input())
    for i in range(T):
        L, R = list(map(int, input().split()))
        ans = [0]*3
        for i in range(L, R+1):
            if "5" in str(i):
                ans[0]+=1
            if "20" in str(i):
                ans[1]+=1
            if "520" in str(i):
                ans[2]+=1
        print(" ".join(map(str, ans)))

def water_healthy():
    n,m,a,b=list(map(int, input().split()))
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()
    print(h)
    ans = 0
    i = 0
    visited = [0]*n
    while True:
        i = i%n
        if h[i]<m:
            ans+=1
            h[i]+=a
            if h[i]>=m:visited[i]=1
            for j in range(n):
                if j!=i:
                    h[j]+=b
                if h[j]>=m:
                    visited[j]=1
        if h[i]>=m:
            visited[i]=1

        if sum(visited)==n:
            break
        i+=1
        print(i)
        print(h)
    print(ans)

def plan_fight():
    t, n = list(map(int, input().split()))
    for i in range(t):
        total = n
        hurt = input().split()
        count_1 = hurt.count("1")
        ans = 0
        if count_1 //2 >0:
            ans += count_1//2
            if total > 2*ans: total -=ans*2
        if total > 0:ans+=total
        print(ans)

def activity_manage():
    n = int(input())
    activity = ['']*n
    for i in range(n):
        activity[i] = input()
    limit_act = [[]for i in range(3)]
    for i in range(3):
        limit_act[i] = list(map(int, input().split()))
    limit = copy.deepcopy(limit_act)
    print(limit_act)
    visitied = [0]*n
    for i in range(n):
        act = activity[i]
        if len(act)==1 and visitied[i]==0:
            if act=="A":limit[0][0]-=1
            elif act=="B":limit[1][0]-=1
            elif act=="C":limit[2][0]-=1
            visitied[i] = 1
        else:
            if "A" in act and limit[0][0]>0 and visitied[i]==0:
                limit[0][0]-=1
                visitied[i] = 1
            if "B" in act and limit[1][0]>0 and visitied[i]==0:
                limit[1][0]-=1
                visitied[i] = 1
            if "C" in act and limit[2][0]>0 and visitied[i]==0:
                limit[2][0]-=1
                visitied[i] = 1
    if sum(visitied)!=n:
        print("NO")
        print(sum(visitied))
    else:
        print(limit)
        print(limit_act)
        cost = 0
        for i in range(3):
            cost+=(limit_act[i][0]-limit[i][0])*limit[i][1]
        print("YES")
        print(cost)

def passage_flow():
    n = int(input())
    R = list(map(int, input().split()))
    R.insert(0, None)
    average = [0]*n
    median = [0]*n
    now = 0
    for i in range(1, n+1):
        print(i)
        now += R[i]
        average[i-1] = math.ceil(now/i)
        sort_R = sorted(R[1:i+1])
        mid = i//2
        print(mid)
        print(sort_R)
        if i%2==0:

            median[i-1] = math.ceil((sort_R[mid]+sort_R[mid-1])/2)
        else:
            median[i-1] = sort_R[mid]
    print(average)
    print(median)

def solve():
    T = int(input())
    for i in range(T):
        n,m = list(map(int, input().split()))
        graph = defaultdict(list)
        indegree = [0 for _ in range(n+1)]
        node_cnt = n
        eq_map = {}
        for _ in range(m):
            a, op,b = input().split()
            a, b = int(a), int(b)
            if a in eq_map:a = eq_map[a]
            if b in eq_map:b = eq_map[b]
            if op =='<':
                graph[a].append(b)
                indegree[b]+=1
            elif op == '>':
                graph[b].append(a)
                indegree[a]+=1
            else:
                if a in eq_map and b in eq_map: node_cnt+=1
                if a in eq_map:eq_map[b] = a
                elif b in eq_map:eq_map[a] = b
                else:
                    eq_map[a] = a
                    eq_map[b] = a
                node_cnt-=1





if __name__ == '__main__':
    passage_flow()
