import heapq
from math import inf

'''
- 迪杰斯特拉算法-加权有向图或者无向图
- 步骤
    初始化：
        1：创建一个集合S，用于存放已经找到最短路径的顶点
        2：对于每个顶点v，初始化其最短路径为无限大，表示暂时未知
        3：设定源点source的最短路径为0，因为从源点到自身的距离为0
    重复直到找到从源点到其他所有其他点的最短路径
        1：从集合v-s（即所有未找到最短路径的顶点）中选择一个距离source最近的顶点，将其加入s（python使用最小堆来选择最近点）
        2：对于从u出发的每条边(u,v)检查是否通过u能够到达v的更短路径，如果是，则更新v的最短路径
    结束条件：当所有顶点都加入集合s时，算法结束

'''

def relation():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    graph ={i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
    ans = []
    visited = set()
    for start, end in queries:
        if dfs(graph, start, end, visited):ans.append(True)
        else:ans.append(False)
    return ans

def dfs(graph, start, end, visited):
    if start == end:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited and dfs(graph, neighbor, end):
            return True
    return False

def djstl(matrix, start, end, n, m):
    visited = [[False]*m for _ in range(n)]
    distance = [[inf]*m for _ in range(n)]
    distance[start][end] = 0
    h = []
    heapq.heappush(h, (0, start, end))
    while h:
        dist, start, end = heapq.heappop(h)
        if visited[start][end]: continue
        visited[start][end] = True
        for i, j in ((start-1, end), (start+1, end), (start, end-1), (start, end+1)):
            if i<0 or j<0 or i>=n or j>=m or visited[i][j]:continue
            if matrix[i][j] == 'S' or matrix[i][j] == 'E' or matrix[i][j] == 'C' or matrix[i][j]=='B':w=0
            else:w = matrix[i][j]
            if distance[start][end]+w < distance[i][j]:
                distance[i][j] = distance[start][end]+w
                heapq.heappush(h, (distance[i][j], i ,j))
    return distance

def graph_cost():
    n, m = map(int, input().split())
    matrix = [input().split() for _ in range(n)]
    C = []
    si,sj, ei,sj = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'C':
                C.append((i, j))
            if matrix[i][j] == 'S':
                si, sj = i, j
            if matrix[i][j] == 'E':
                ei, ej = i, j
    cost = inf
    for ci, cj in C:
        dis = djstl(matrix, ci, cj)
        if dis[si][sj]==inf or dis[ei][ej]==inf:
            return -1
        else:
            cost = min(cost, dis[si][sj]+dis[ei][ej])
    return cost

def travel_graph():
    '''
    https://mp.weixin.qq.com/s/8qv-jYrDzgnsMBoVSHIyig
    '''
    pass

def similar_count():
    '''
    https://mp.weixin.qq.com/s/gGZVTDkLYL2_C3_u-N2alA
    节点的度数：一个节点连接的边的数量
    跟节点=子节点数量
    非根节点=子节点数量+1（父节点的变）
    '''
    n = int(input())
    deg = {}
    for i in range(n-1):
        u, v = map(int, input().split())
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1

    print(f"deg {deg}")
    mp = {}
    for i in range(1, n+1):
        if i == 1:
            mp[deg[i]] = mp.get(deg[i], 0) + 1
        else:
            mp[deg[i] - 1] = mp.get(deg[i] - 1, 0) + 1

    print(f"mp {mp}")
    ans = 0
    for v in mp.values():
        ans += v * (v - 1) // 2
    print(ans)
    return ans

class UnionFind:
    def __init__(self, n):
        # 初始化默认自己指向自己
        self.father = [i for i in range(n)]
        self.rank = [0] * n
    
    # 并查集里寻根的过程
    def find(self, u):
        if self.father[u]!=u:
            # 路径压缩
            self.father[u] = self.find(self.father[u])
        return self.father[u]
    
    # 判断u和v是否找到同一个根
    def is_same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u==v

    # 将v->u这条边加入并查集
    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u==v: return 
        self.father[v] = u


def max_land():
    '''
    https://mp.weixin.qq.com/s/-JHuxZML2XRAmqUiAuMiQA
    - 首先计算出每一个陆地联通块的大小和位置，这里直接在原图上修改，即第一个连通块的所有单元各记为1
    - 计算出每一个海洋连通块的大小和第一个单元格的位置
    - 遍历海洋连通块，每一个连通块使用dfs将单元格设置为True，然后遍历这些单元格的周围将连接的陆地接上
    '''
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(list(input()))

    def dfs_land(x, y, visited, mark):
        if x<0 or y<0 or x>=n or y>=m or visited[x][y] or s[x][y]==mark or s[x][y]==".":return 0
        visited[x][y] = True
        s[x][y]=mark
        size = 1
        size+=dfs_land(x+1, y, visited, mark)
        size+=dfs_land(x-1, y, visited, mark)
        size+=dfs_land(x, y+1, visited, mark)
        size+=dfs_land(x, y-1, visited, mark)
        return size

    def dfs(x,y, visited, target):
        if x<0 or y<0 or x>=n or y>=m or visited[x][y] or s[x][y]!=target:return 0
        visited[x][y] = True
        size = 1
        size+=dfs(x+1, y, visited, target)
        size+=dfs(x-1, y, visited, target)
        size+=dfs(x, y+1, visited, target)
        size+=dfs(x, y-1, visited, target)
        return size

    visited = [[False] * m for _ in range(n)]
    land_block = {}
    sea_block = {}
    max_land_size = 0
    mark = 1
    for i in range(n):
        for j in range(m):
            if s[i][j]=="#" and not visited[i][j]:
                size = dfs_land(i, j, visited, mark)
                land_block[mark] = size
                max_land_size = max(max_land_size, size)
                mark += 1

    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if s[i][j]=="." and not visited[i][j]:
                size = dfs(i,j,visited, ".")
                sea_block[(i,j)]=size

    max_size_after_ignition = max_land_size
    for (si, sj), sea_size in sea_block.items():
        adjance_block = set()
        visited = [[False]*m for _ in range(n)]
        dfs(si, sj, visited, ".")
        for i in range(n):
            for j in range(m):
                if visited[i][j] and s[i][j]==".":
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        ni, nj = i+dx, j+dy
                        if 0<=ni<n and 0<=nj<m and s[ni][nj]!="." and not visited[ni][nj]:
                                adjance_block.add(s[ni][nj])

        total_size = sea_size
        for block in adjance_block:
            total_size+=land_block[block]
        max_size_after_ignition = max(max_size_after_ignition, total_size)
        print(max_size_after_ignition)
    return max_size_after_ignition


'''
- 给出一个有向图，将这个有向图转换为线性的排序，就叫拓扑排序（必须无环）
- 实现拓扑排序的两种算法：BFS和DFS
- BFS步骤：
    1. 找到入度为0的节点，加入结果集
    2. 将该节点从图中移除
'''
def loop():
    '''
    - 拓扑排序+GTO博弈
    -基环树-在一棵树的基础上加上一个环，n个节点n条边'''
    n, x = map(int, input().split())
    graph = [[]for _ in range(n+1)]
    indegre = [0]*(n+1)
    for i in range(1, n+1):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegre[u]+=1
        indegre[v]+=1
    indegre_one = []
    for i in range(1, n+1):
        if indegre[i]==1:
            if i==x:
                return "xiao"
            indegre_one.append(i)
    if len(indegre_one)==0:
        return "Draw"
    elif len(indegre_one)%2==0:
        return "xiao"
    else:
        return "da"

def reliance():
    '''文件依赖找出执行顺序'''
    n, m = map(int, input().split())
    indegre = [0]*n
    res = []
    umap = {}
    for i in range(m):
        s, t = map(int, input().split())
        indegre[t]+=1
        umap.setdefault(s, []).append(t)
    q = []
    for i in range(n):
        if indegre[i]==0:
            q.append(i)
    while q:
        cur = q.pop(0)
        res.append(cur)
        if cur in umap:
            for file in umap[cur]:
                indegre[file]-=1
                if indegre[file]==0:q.append(file)

    if len(res)==n:
        for i in range(n-1):
            print(res[i], end=" ")
        print(res[n-1])
    else:
        print(-1)




if __name__ == '__main__':
    reliance()


        
    
