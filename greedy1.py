a= input()# 이코테 왕실 나이트

x = int(ord(a[0])) - int(ord(a[0]))+1
y = int(a[1])
count =0
move = [(2,1), (-2,1), (2,-1), (1,2), (-1, 2), (1, -2), (-1, -2), (-2, -1)]

for i in range(len(move)):
  dx = x + move[i][0]
  dy = y + move[i][1]

  if dx >=1 and dx <=8 and dy <8 and dy >= 1:
    count +=1
  else:
    continue

print(count)
