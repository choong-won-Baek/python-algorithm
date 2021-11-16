# 음료수 얼려 먹기 문제 
n, m = map(int,input().split()) # 가로 세로 줄 입력 

graph =[] # 입력받을 그래프 생성 

for i in range(n): # 그래프에 한 줄 씩 입력 
  a = list(map(int, input()))
  graph.append(a)

count =0 # 총 얼음 갯수 
def check(x, y): # 특정 지점이 0 이면 무조건 얼음이 생기는데 재차함수를 BFS혹은 DFS로 얼음이 얼마나 큰지를 확인 한다. 0주위에 모든 0을 찾아서 1을 찾고 얼음 하나가 생긴다는 의미로 true 반환 
  if x>-1 and x<n and y>-1 and y<m: #얼음 틀 크기 범위
    if graph[x][y] == 0:
      graph[x][y]=1
      check(x-1,y)
      check(x+1,y)
      check(x,y-1)
      check(x,y+1)
      return True
  return False

for i in range(n):#모든 얼음 틀 구멍하나씩 확인 
  for j in range(m):
    if check(i,j) == True:
      count +=1

print(count)
