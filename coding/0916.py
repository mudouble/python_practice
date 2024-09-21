import math
from collections import deque
def fun1():
    '''求丢垃圾的最短路径，首先将终点垃圾站加入队列，然后计算垃圾站到各个点的最短距离，最后再将起点的距离加起来
    使用BFS'''
    n, m = map(int, input().split())
    grid = [[0]*m for _ in range(n)]
    house = []
    dis = [[-1]*m for _ in range(n)]
    for i in range(n):
        lists = list(map(int, input().split()))
        for j in range(m):
            if lists[j]==0:
                house.append((i, j))
                dis[i][j] = 0
            grid[i][j]=lists[j]

    while house:
        i, j = house.pop(0)
        for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=x<n and 0<=y<m and grid[x][y]!=-1 and dis[x][y]==-1:
                dis[x][y]=dis[i][j]+1
                house.append((x, y))
    res =0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and dis[i][j]!=-1:
                res+=dis[i][j]
    print(res)

def fun2():
    '''堆盒子, 底下的盒子的长宽高必须大于上面的盒子，求最高高度'''
    n = int(input())
    boxes = []
    res = [0]*n
    for i in range(n):
        boxes.append(list(map(int, input().split())))
    box_sorted = sorted(boxes,key=lambda x:x[-1], reverse=True)
    for i in range(n):
        res[i]=box_sorted[i][2]
        max_len, max_wid = box_sorted[i][0], box_sorted[i][1]
        for j in range(i+1,n):
            if box_sorted[j][0]<max_len and box_sorted[j][1]<max_wid:
                res[i]+=box_sorted[j][2]
                max_len, max_wid = box_sorted[j][0], box_sorted[j][1]
    print(max(res))

def fun3():
    n = int(input())
    m = int(input())
    station = []
    for i in range(m):
        station.append(list(map(int, input().split())))

    station.sort()
    res = [0]*m

    for i in range(m):
        start, end, value = station[i]
        res[i]=value
        for j in range(i+1, m):
            if station[j][0]>=end+1 and end<=n:
                res[i]+=station[j][2]
                end = station[j][1]
    print(max(res))


def fun4():
    n = int(input())
    origin = list(map(int, input().split()))
    m = int(input())
    refence = list(map(int, input().split()))
    index = 0
    while index<m and index<n:
        if origin[index]==refence[index]:
            origin[index]=""
        index+=1
    dic = {}
    for item in origin:
        if item =="":continue
        dic[item]=dic.get(item,0)+1
    dic = sorted(dic.items(), key=lambda x:(x[1], x[0]), reverse=True)
    for item in dic:
        print(item[0], end=" ")



def fun5():
    n, m, k, l = map(int, input().split())
    relation ={}
    for i in range(m):
        x, y = map(int, input().split())
        relation.setdefault(x,[]).append(y)
        relation.setdefault(y,[]).append(x)

    k_relation = relation[k]
    commond = {}
    for people in relation.items():
        if people[0] in k_relation or people[0]==k:continue
        for i in people[1]:
            if i in k_relation:
                commond[people[0]]=commond.get(people[0],0)+1
    commond = sorted(commond.items(), key=lambda x:x[1], reverse=True)
    commond = dict(commond)
    if l>len(commond):
        ans = [0]*(l-len(commond))
        print(" ".join(str(x) for x in list(commond.keys()) + ans))
    else:
        print(" ".join(str(x) for x in commond.keys()[:l+1]))


def fun6():
    n,k = map(int, input().split())
    compamy_x, compamy_y = map(int, input().split())
    clients = []
    for i in range(n):
        clients.append(list(map(int, input().split())))
    clients.sort(key = lambda x:x[-1])

    def calculate_distance(point1, point2):
        distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
        return distance

    dp ={}
    def dfs(i, j):
        if (i,j) in dp:return dp[(i,j)]
        dis = calculate_distance((clients[i][0], clients[i][1]), (compamy_x,compamy_y))
        if i==n-1:return dis
        ans = dfs(i+1, k-1)+dis+calculate_distance((compamy_x, compamy_y), (clients[i+1][0], clients[i+1][1]))
        if j>0:
            ans = min(ans, dfs(i+1, j-1)+calculate_distance((clients[i][0], clients[i][1]), (clients[i+1][0], clients[i+1][1])))
        dp[(i,j)] = ans
        return ans

    print(round(dfs(0,k-1)+calculate_distance((compamy_x, compamy_y), (clients[0][0], clients[0][1])),1))








if __name__ == '__main__':
    fun5()

