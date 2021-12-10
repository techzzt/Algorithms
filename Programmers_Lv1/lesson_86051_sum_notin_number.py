# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:21:51 2021

@author: keun
"""

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer