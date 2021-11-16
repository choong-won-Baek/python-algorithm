a = input()
A = list(a)
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Num = []

for i in A:
    if i in num:
        Num.append(i)
        A.remove(i)
result = A + Num
Result = ''.join(result)
print(Result)
