from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)
            
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()