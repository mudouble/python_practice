import math


def prime():
    '''最小生成树'''
    v, e = map(int, input().split())
    nums = 10001
    grid = [[nums]*(v+1) for _ in range(v+1)]
    for i in range(e):
        x, y, k = map(int, input().split())
        grid[x][y] = k
        grid[y][x] = k
    
    min_dist = [nums]*(v+1)
    is_in_tree = [False]*(v+1)
    for i in range(1, v):
        cur = i
        # min_val = math.inf
        # for j in range(1, v+1):
        #     if not is_in_tree[j] and min_dist[j] < min_val:
        #         min_val = min_dist[j]
        #         cur = j
        # print(f" i {i} cur {cur} min_dist {min_dist}")
                
        is_in_tree[cur] = True
        for j in range(1, v+1):
            if not is_in_tree[j] and grid[cur][j]<min_dist[j]:
                min_dist[j] = grid[cur][j]
        print(f"after min_dist {min_dist}")
                
    res = 0
    for i in range(2, v+1):
        res += min_dist[i]

    print(res)

class Edge:
    def __init__(self, l, r, val):
        self.l = l
        self.r = r
        self.val = val

n = 10001
father = list(range(n))
def init():
    global father
    father = list(range(n))

def find(u):
    if u!=father[u]:
        father[u] = find(father[u])
    return father[u]

def join(u,v):
    u = find(u)
    v = find(v)
    if u!=v:
        father[u] = v

def kruskal():
    v, e = map(int, input().split())
    edges = []
    for i in range(e):
        x, y, k = map(int, input().split())
        edges.append(Edge(x,y,k))
    edges.sort(key=lambda edge:edge.val)
    init()
    res_val = 0
    for edge in edges:
        x = find(edge.l)
        y = find(edge.r)
        if x!=y:
            res_val += edge.val
            join(x,y)
    print(res_val)
    return res_val



    



    
if __name__ == '__main__':
    kruskal()