import math 

# M, N 입력
m, n = map(int, input().split())
array = [True for i in range(100001)]
array[1] = 0 # 1은 소수가 아님 

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False 
            j += 1
    
# M ~ N 모든 소수 출력 
for i in range(m, n + 1):
    if array[i]:
        print(i)