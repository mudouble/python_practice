import math


def func():
    n = int(input())
    relation = []
    for i in range(n):
        relation.append(list(map(int, input().split())))
    res = []
    visited = [0]*n
    for i in range(n):
        if visited[i]==1:continue
        temp = [i]
        visited[i]=1
        for j in range(i+1, n):
            if i not in relation[j]:
                visited[j]=1
                temp.append(j)
        res.append(temp)
    print(res)
    return res

def func3():
    n,m,k = map(int, input().split())
    G = [[] for _ in range(1010)]
    for _ in range(n):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    print(G)
    def dfs(u, vst, stp):
        nonlocal ans
        if vst[u] or stp>k:return
        vst[u] = True
        ans+=1
        for next in G[u]:
            dfs(next, vst, stp+1)

    ans = 0
    dfs(m, [False]*1010, 0)
    print(ans-1)



if __name__ == '__main__':
    # func3()
    print(-10/3)
    print(-10%3)
    print(-10%-3)
    print(10%3)

