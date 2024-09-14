from collections import deque


class FindUnion:

    def __init__(self, n):
        self.father = [i for i in range(n+1)]

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v: return
        self.father[v] = u

def fun1():
    n = int(input())
    find_union = FindUnion(n)
    for i in range(n):
        u, v = map(int, input().split())
        if find_union.is_same(u,v):
            print(u,v)
            return str(u)+" "+str(v)
        else:
            find_union.join(u, v)


def fun2():
    n = int(input())
    find_union = FindUnion(n)
    
    def get_remove_edge(edges):
        for i in range(n):
            if find_union.is_same(edges[i][0], edges[i][1]):
                print(edges[i][0], edges[i][1])
                return 
            else:
                find_union.join(edges[i][0], edges[i][1])
    
    def is_tree_after_remove(edges, delete_edge):
        for i in range(n):
            if i==delete_edge:continue
            if find_union.is_same(edges[i][0], edges[i][1]):return False
            find_union.join(edges[i][0], edges[i][1])
        return True
    
    indegre = [0]*(n+1)
    edges = []
    for i in range(n):
        u,v = map(int, input().split())
        indegre[v]+=1
        edges.append([u,v])

    temp = []
    for item in indegre[::-1]:
        if item[-1]==2:
            temp.append(item[0])

    while temp:
        if is_tree_after_remove(edges, temp[0]):
            print()


def func2():
    '''字符串处理'''
    ans, index, strs = [], 0, ""
    while True:
        s = input()
        if s=="end":
            break
        k = s.split()
        if len(k)==2:
            oper, strs = k
        else:
            oper = s
        if oper == "insert":
            ans = ans[:index] + list(strs) + ans[index:]
            index += len(strs)

        elif oper == "delete":
            num = int(strs)
            if num <= index:
                ans = ans[:index - num] + ans[index:]
                index -= num

        elif oper == "move":
            num = int(strs)
            if num < 0 and abs(num) <= index:
                index+=num
            if num > 0 and num <= len(ans) - index:
                index += num

        elif oper == "copy":
            temp = ans[:index]
            ans = temp + temp + ans[index:]


    ans.insert(index, "|")
    print("".join(ans))

def func3():
    '''广度优先，传播的时间
    https://kamacoder.com/problempage.php?pid=1214
    '''
    n = int(input())
    m = int(input())
    j, k = map(int, input().split())
    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))

    visited = [[-1]*n for _ in range(m)]
    for x in range(m):
        for y in range(n):
            if grid[x][y]==0:visited[x][y]=-2
            
    visited[j][k] = 0
    que = deque()
    que.append([j, k])
    print(f"que {que}")
    while que:
        x, y = que.popleft()
        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if nx<0 or ny<0 or nx>=m or ny>=n or visited[nx][ny]==-2 :continue
            if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + grid[x][y]:
                visited[nx][ny] = visited[x][y]+grid[x][y]
                print(f"nx ny {nx, ny} x, y {x,y}")
                print(f"visited {visited}")
                que.append([nx, ny])
    res =0
    for i in range(m):
        for j in range(n):
            if visited[i][j]==-1:
                return 0
            if visited[i][j]==-2:
                continue
        res = max(res, visited[i][j])
    print(res)



if __name__ == '__main__':
    # fun1()
    func3()
