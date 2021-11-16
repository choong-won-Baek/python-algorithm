from collections import Counter
a = input()
result=[]
sum=0

for i in a:
  if i.isalpha():
    result.append(i)
  else:
    sum +=int(i)

result.sort()
if sum>0:
  result.append(str(sum))
print(''.join(result))
