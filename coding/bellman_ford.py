'''
Bellman_ford算法：对所有的边进行|V|-1次松弛操作，从而求得目标最短路径
- 适合包含负权边的图，而Dijkstra适合所有边权重非负的图
'''
import math
from collections import deque


def bellman_ford():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    start, end = 1, n
    min_dist = [math.inf]*(n+1)
    min_dist[start] = 0
    for i in range(1, n):
        for u, v, w in edges:
            if min_dist[u]!=math.inf and min_dist[v]>min_dist[u]+w:
                min_dist[v] = min_dist[u]+w
    print(min_dist)
    
    if min_dist[end]==math.inf:print("unconnected")
    else:
        print(min_dist[end])

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w
        
def bellman_ford_queue():
    '''
    从源节点开始，对相接的边进行松弛，然后再将相接的边的节点加入队列
    :return:
    '''
    n, m = map(int, input().split())
    is_in_queue = [False]*(n+1)
    edges = {}
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.setdefault(u, []).append(Edge(v,w))
    start = 1
    min_dist = [math.inf]*(n+1)
    min_dist[start] =0
    que = deque()
    que.append(start)
    while que:
        node = que.popleft()
        is_in_queue[node] = False
        for edge in edges.get(node, []):
            if min_dist[edge.v] > min_dist[node]+edge.w:
                min_dist[edge.v] = min_dist[node]+edge.w
                if not is_in_queue[edge.v]:
                    que.append(edge.v)
                    is_in_queue[edge.v] = True
    if min_dist[n] == math.inf:
        print("unconnected")
    else:
        print(min_dist[n])

def bellamn_ford_negative():
    '''有负权环'''
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    start = 1
    end = n
    min_dist = [math.inf]*(n+1)
    min_dist[start] = 0
    flag = False
    for i in range(1, n+1):
        for u, v, w in edges:
            if i<n:
                if min_dist[u]!=math.inf and min_dist[v]>min_dist[u]+w:
                    min_dist[v] = min_dist[u]+w
            elif min_dist[u]!=math.inf and min_dist[v]>min_dist[u]+w:flag = True

    if flag:print("circle")
    elif min_dist[n]==math.inf:print("unconnected")
    else:
        print(min_dist[end])

def bellaman_ford_limit():
    '''单源有限最短路径'''
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    src, dst, k = map(int, input().split())
    min_dist = [math.inf]*(n+1)
    min_dist[src] = 0
    for i in range(k+1):
        for u, v, w in edges:
            if min_dist[u]!=math.inf and min_dist[v]>min_dist[u]+w:
                min_dist[v] = min_dist[u]+w
    if min_dist[dst]==math.inf:print("unreachable")
    else:
        print(min_dist[dst])
    
def floyd():
    '''多源最短路径问题
    多个起点到多个终点的多条最短路径问题
    定义一个三维数组，初始化为最大值，然后计算i到j经过k个顶点的最短距离
    因为k只是记录上一层有没有更短的距离，并不需要记录k-2等
    '''
    n,m = map(int, input().split())
    grid = [[10005 for i in range(n+1)] for j in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        grid[u][v] = w
        grid[v][u] = w


    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])

    z = int(input())
    for i in range(z):
        start, end = map(int, input().split())
        if grid[start][end]==10005:print("unreachable")
        else:
            print(grid[start][end])



if __name__ == '__main__':
    floyd()