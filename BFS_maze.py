#미로 탈출 
from collections import deque

n, m = map(int,input().split()) # 가로 세로 줄 입력 

graph =[] # 입력받을 그래프 생성 
count =0
for i in range(n): # 그래프에 한 줄 씩 입력 
  a = list(map(int, input()))
  graph.append(a)

def bfs(x, y): # bfs를 활용한 풀이 
  queue = deque() # 큐 생성 
  queue.append((x,y)) # 큐에 (0,0) 삽입
  dx = (-1, 1, 0, 0) # 상하 좌우 이동을 위한 좌표
  dy = (0, 0, -1, 1)

  while queue: # 큐가 없을 때까지 
      x, y = queue.popleft()# 큐에 든 숫자 꺼내서
      for i in range(4):# 이동 좌표로 이동해본다
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx < 0 or nx >=n or ny<0 or ny >=m:# 이동해본 숫자 중에 범위를 벗어나면 스킵
          continue
        if graph[nx][ny] == 0:# 0이면 스킵 
          continue
        if graph[nx][ny] == 1: # 1이면 이동된 위치에
          graph[nx][ny]=graph[x][y]+1 # 그전 숫자에 1을 더해서 여태 온 거리 기록 
          queue.append((nx, ny)) # 이동된 위치 큐에 넣기 
  return graph[n-1][m-1] # 큐가 없어지면 목적지 도달이기 때문에 총 거리가 측정된 맨 마지막 숫자 리턴 


print(bfs(0,0))
