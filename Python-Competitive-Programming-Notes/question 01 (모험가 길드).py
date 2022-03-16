# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:17:20 2022

@author: keun
"""
##### 모험가 길드 #####
# 모험가들로부터 측정한 공포도를 기준으로 공포도 x에 대해 x명 이상으로 구성된 모험가 그룹 형성 
# N 명의 모험가에 대해 모험 가능한 최대 그룹 수를 반환 

n = int(input())
data = list(map(int, input().split()))

data.sort()

# 현재 총 그룹의 수 
result = 0

# 모험가의 수 
count = 0

for i in data:
    count += 1 
    if i >= count:
        result += 1
        count = 0

print(count)
