from collections import deque


def func():
    N = 8

    def bfs(start, end):
        if start[0]==end[0] and start[1]==end[1]:
            return 0
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                pos = queue.popleft()
                for i in [(2,1), (-2,1),(2,-1),(-2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]:
                    x = pos[0]+i[0]
                    y = pos[1]+i[1]
                    if(x==end[0] and y==end[1]):
                        return step+1
                    if x>=1 and x<=N and y>=1 and y<=N:
                        if (x,y)not in visited:
                            visited.add((x,y))
                            queue.append((x, y))
            step+=1
        return -1
    ans = bfs((1,1), (8,8))
    print(ans)

if __name__ == '__main__':
    func()
