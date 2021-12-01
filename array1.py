#선택정렬 기본
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]# 무작위 정렬

for i in range(len(array)):# 정렬 범위 만큼 반복 
    min_index = i # 반복 당사자, 기준이 되는 요소
    for j in range(i+1, len(array)): # 기준 다음 요소들 만큼 반복 
        if array[min_index] > array[j]:# 기준 보다 작은 요소가 있다면 
            min_index = j# 보다 작은 요소가 기준이 된다, 한 바퀴 돌고 나면 제일 작은 값이 min_index가 된다
    array[i], array[min_index] = array[min_index], array[i] #순차적인 i와 제일 작은 값이 된 min_index를 바꾼다. 

print(array)#i가 처음 부터 끝까지 돌면 오름차순 정렬이된다.
    
