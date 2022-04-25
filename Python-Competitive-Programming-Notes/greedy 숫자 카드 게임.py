# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:49:49 2022

@author: keun
"""

# n = row, m = column 
n, m = map(int, input().split())

# save result 
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    
    # min value in N
    min_value = min(data)
    
    # compare with each row 
    result = max(result, min_value)
    

print(result)