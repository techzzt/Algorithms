# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:05:03 2022

@author: keun
"""

data = input()

# int type으로 변경 
total = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or total <= 1:
        total += num 
    else:
        total *= num
    
print(total) 