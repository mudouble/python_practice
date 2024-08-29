import heapq
import json
import sys


def extract_filenames_extensions_versions():
    # 输入必须是双引号的
    filenames_list = json.loads(input())
    ans = []
    for file_item in filenames_list:
        filename_sprint, filename, extension_name, sprint_number = "", "", "", 0
        if "." in file_item:
            filename_sprint, extension_name = file_item.split(".")
        sprint_number = 0
        if filename_sprint is not None and "_" in filename_sprint:
            filename, sprint_name = filename_sprint.split("_")
            sprint_number = int(sprint_name.split("v")[-1])
        ans.append((filename, extension_name, sprint_number))
    return ans

def directory_name():
    parent_dir = input().split(" ")
    sun_dir = input().split(" ")
    target_dir = input()
    ans = []
    dir = {}
    for (par, sun) in zip(parent_dir, sun_dir):
        dir[par] = sun
    ans.append(target_dir)
    while target_dir in dir:
        ans.append(dir[target_dir])
        target_dir = dir[target_dir]
    return " ".join(ans)

def directory_name_queue():
    parent_dir = input().split(" ")
    sun_dir = input().split(" ")
    target_dir = input()
    queue = []
    ans = []
    queue.append(target_dir)
    while queue:
        target_dir = queue.pop(0)
        print(target_dir)
        print(queue)
        ans.append(target_dir)
        print(ans)
        for i in range(len(parent_dir)):
            if parent_dir[i] == target_dir:
                queue.append(sun_dir[i])

    return " ".join(ans)

def dfs(graph, start, target, visited):
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

def process_queries(n, edges, queries):
    input = sys.stdin.read
    data = input().splitlines()
    n, d = map(int, data[0].split())
    edges = [tuple(map(int, data.split())) for data in data[1:d+1]]
    q = int(data[d+1])
    queries = [tuple(map(int, data.split())) for data in data[d+2:d+2+q]]

    graph = {i: [] for i in range(n)}
    print("graph:  ", graph)
    for u, v in edges:
        graph[u].append(v)
    print("after: ", graph)
    result = []
    for start, target in queries:
        visited = set()
        if dfs(graph, start, target, visited):
            result.append(1)
        else:
            result.append(0)
    for result in result:
        print(result)
    return result


def travel_price():
    total = int(input())
    from collections import defaultdict
    price_times = defaultdict(list)
    while True:
        line = input()
        if line == "":
            break
        line = line.strip().split(" ")
        price_times[int(line[0])].append(int(line[1]))
    sorted_price_times = sorted(price_times.items(), key=lambda x: x[0])
    count = 0
    ans = 0
    for (price, times) in sorted_price_times:
        print(count, price, times)
        for time in times:
            for i in range(time):
                count += price
                if total < count: break
                ans += 1
    return ans

def linked_list():
    link_1 = input()
    link_2 = input()
    count = 0
    ans = []
    for index_1 in range(len(link_1)):
        for index_2 in range(index_1 + 1, len(link_1)):

            if link_1[index_1:index_2] in link_2:

                if len(link_1[index_1:index_2]) > count:
                    count = len(link_1[index_1:index_2])
                    ans=link_1[index_1:index_2]
    print(count)
    return ans

def solve(st_i, st_j, n ,m, matrix):
    from math import inf
    distance = [[inf]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    distance[st_i][st_j] = 0
    h = []
    heapq.heappush(h,[0, st_i, st_j])
    while h:
        d, i, j = heapq.heappop(h)
        if visited[i][j]:continue
        visited[i][j] = True
        for ni, nj in ((i+1, j), (i, j+1), (i-1, j-1),(i, j-1)):
            if ni<0 or nj<0 or ni>=n or nj>=m or visited[ni][nj] or matrix[ni][nj] == 'B': continue
            w = 0
            if matrix[ni][nj] == 'C' or matrix[ni][nj] == 'E' or matrix[ni][nj] == 'S':w = 0
            else: w = int(matrix[ni][nj])
            if distance[ni][nj] > w+distance[i][j]:
                distance[ni][nj] = distance[i][j]+w
                heapq.heappush(h, [distance[ni][nj], ni, nj])
    return distance

def ore_cost():
    from math import inf
    n, m = map(int, input().split())
    matrix = [input().split() for _ in range(n)]
    C = []
    res = inf
    si, sj, ei, ej = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'C':
                C.append((i, j))
            if matrix[i][j] == 'S':
                si, sj = i, j
            if matrix[i][j] == 'E':
                ei, ej = i, j
    for ci, cj in C:
        dis = solve(ci, cj, n, m, matrix)
        if dis[si][sj] == inf or dis[ei][ej] == inf:
            continue
        else:
            res = min(res, dis[si][sj] + dis[ei][ej])
    if res == inf:return -1
    else:return res










if __name__ == '__main__':
   res = ore_cost()
   print(res)

