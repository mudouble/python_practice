import heapq
from math import inf

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

def binary_search(nums, target, ans):

    middle = len(nums)//2
    if target == nums[middle]:
        ans.append("Y")
        return ans
    elif middle == 0:
        ans.append("N")
        return ans
    elif target>nums[middle]:
        ans.append("R")
        binary_search(nums[middle+1:], target, ans)
    elif target<nums[middle]:
        ans.append("L")
        binary_search(nums[:middle], target, ans)
    return ans
def tree_path():
    nums = sorted(map(int, input().split()))
    target = int(input())
    temp = []
    temp.append("S")
    ans = binary_search(nums, target, temp)
    print("".join(ans))
    return "".join(ans)

def count_consecutive_goals(data):
    count=0
    ans = 0
    for i in data:
        if i=="1":
            count+=1
            ans = count if count>ans else ans
        else:
            count=0
    return ans
def ability_sort():
    n, m = map(int, input().split())
    train_data = input().split()
    dicts = {i:[]for i in range(n)}
    for i in range(n):
        data = train_data[i]
        goals = data.count("1")
        consecutive_goals = count_consecutive_goals(data)
        conceding_goals = [index for index in range(m) if data[index] == "0"]
        dicts[i] = [goals, consecutive_goals, conceding_goals]

    sorted_goals = dict(sorted(dicts.items(), key=lambda item:-item[1][0]))
    sorted_consecutive_goals = dict(sorted(sorted_goals.items(), key=lambda item:-item[1][1]))
    print(sorted_consecutive_goals)
    for i in range(1, n):
        if sorted_consecutive_goals[i][1] == sorted_consecutive_goals[i-1][1] and \
                sorted_consecutive_goals[i][0]==sorted_consecutive_goals[i-1][0] and \
                sorted_consecutive_goals[i][2] != sorted_consecutive_goals[i - 1][2]:
            for s, t in zip(sorted_consecutive_goals[i][2], sorted_consecutive_goals[i-1][2]):
                if s>t:
                    print("zhixing ")
                    #调换顺序
                    values = list(sorted_consecutive_goals.values())
                    keys = list(sorted_consecutive_goals.keys())
                    keys[i], keys[i-1] = keys[i-1], keys[i]
                    values[i], values[i-1] = values[i-1], values[i]
                    sorted_consecutive_goals = dict(zip(keys, values))
                    break
    print(sorted_consecutive_goals)
    print([key+1 for key in sorted_consecutive_goals.keys()])
    return [key+1 for key in sorted_consecutive_goals.keys()]

def count_consecutive_brand(data):
    count=0
    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            count+=1
            if count == 2:
                return i+1
        else:
            count=0
    return -1
def eliminate():
    n = int(input())
    strs = "".join(input().split())
    while True:
        index = count_consecutive_brand(strs)
        if index == -1:
            break
        else:
            strs = strs[:index-2]+strs[index+1:]
    if len(strs)==0:
        print(0)
        return 0
    print(" ".join(strs))
    return strs

def eliminate_stack():
    n = int(input())
    cards = input().split()
    stack = []
    for index, c in enumerate(cards):
        stack.append(c)
        if len(stack)>=3 and stack[-1]==stack[-2] ==stack[-3]:
            stack.pop()
            stack.pop()
            stack.pop()
    if len(stack)==0:print(0)
    else: print(" ".join(stack))

def cloud_service():
    m, n = map(int, input().split())
    matrix = [input().split() for _ in range(n)]
    cloud = set()
    for i in range(n):
        if matrix[i][1] == "*":
            cloud.add(matrix[i][0])

    dicts = {c:[0]*2 for c in cloud}
    dicts_temp = {c:[] for c in cloud}
    for i in range(n):
        if matrix[i][1] in cloud:
            dicts_temp[matrix[i][1]].append(matrix[i][0])

    for i in range(n):
        c = matrix[i][1]
        if c in cloud or matrix[i][0] in cloud:
            if matrix[i][2]=="0":
                if matrix[i][0] in cloud:
                    dicts[matrix[i][0]][0]+=int(matrix[i][-1])
                elif c in cloud:
                    dicts[c][0] += int(matrix[i][-1])
            if matrix[i][2]=="1":
                if matrix[i][0] in cloud:
                    dicts[matrix[i][0]][1]+=int(matrix[i][-1])
                elif c in cloud:
                    dicts[c][1] += int(matrix[i][-1])
        else:
            for item, values in dicts_temp.items():
                if matrix[i][1] in values:
                    if matrix[i][2]=="0":dicts[item][0] += int(matrix[i][-1])
                    if matrix[i][2]=="1":dicts[item][1] += int(matrix[i][-1])

    ans = 0
    for item, values in dicts.items():
        if values[0]*5+values[1]*2 > m:
            ans+=1
    print(ans)
    return ans

def cloud_djstl(delayMatrix, faultyNode, n):
    h = [[0, faultyNode]]
    dist = [inf]*n
    dist[faultyNode] = 0
    while h:
        d, u = heapq.heappop(h)
        if d>dist[u]:
            continue
        for v in range(n):
            if delayMatrix[u][v]!=-1 and dist[v]>d+delayMatrix[u][v]:
                dist[v] = d+delayMatrix[u][v]
                heapq.heappush(h, (dist[v], v))
    return dist

def cloud_graph():
    n = int(input())
    delayMatrix = [list(map(int, input().split())) for i in range(n)]
    remainingCapacity = list(map(int, input().split()))
    faultyNode = int(input())
    migrate = int(input())
    dis = cloud_djstl(delayMatrix, faultyNode, n)
    print(dis)
    tmp = [[dis[i], i] for i in range(n)]
    tmp.sort()
    print(tmp)
    res = []
    while migrate>0 and len(tmp)>0:
        d,u = tmp.pop(0)
        if u == faultyNode:
            continue
        res.append(u)
        migrate -= remainingCapacity[u]
    print(" ".join(map(str, res)))
    return " ".join(map(str, res))

def circle():
    n = int(input())
    edges = list(map(int, input().split()))
    







if __name__ == '__main__':
    cloud_graph()









