### bfs 문제풀이 ###

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int,input().split())
G = []

for _ in range(N):
    G.append(list(map(int,input().split())))
Q = deque()

# 처음 익은 토마토는 큐에 추가
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            Q.append((i,j))

mx_list = [-1, 1, 0, 0]
my_list = [0, 0, 1, -1]

while Q:
    x, y = Q.popleft()
    
    for mx, my in zip(mx_list, my_list):
        nx = x + mx
        ny = y + my
        if 0 <= nx <N and 0 <=ny <M and G[nx][ny] == 0:
            Q.append((nx, ny))
            G[nx][ny] = G[x][y]+1 
            
max_days = 0
is_zero = False

# 최대 일 수 확인
for i in range(N):
    for j in range(M):
        if  G[i][j] == 0:
            is_zero = True
        max_days = max(max_days, G[i][j])

if is_zero:
    print(-1)
else:
    print(max_days-1)
