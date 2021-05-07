from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# def dfs(x,y,move_cnt):
#     if (x,y) == (n-1,m-1):
#         return move_cnt
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         if (x, y) == (n - 1, m - 1):
#             return move_cnt
#         else:
#             return False
#     if graph[x][y] == 1:
#         print(x,y,move_cnt)
#         graph[x][y] = 0
#         move_cnt += 1
#         dfs(x-1,y,move_cnt)
#         dfs(x,y-1,move_cnt)
#         dfs(x+1,y,move_cnt)
#         dfs(x,y+1,move_cnt)
#     pass
#
# print(dfs(0,0,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
print(graph)