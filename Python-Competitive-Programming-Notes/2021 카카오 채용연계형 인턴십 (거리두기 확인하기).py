# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:10:23 2022

@author: keun
"""

# https://programmers.co.kr/learn/courses/30/lessons/81302 

from itertools import combinations 

def solution(places):
    answer = []
    
    # save p location 
    for place in places:
        pos = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    pos.append((i, j))
        
        safe = 1
        com = list(combinations(pos, 2))
    
    # check distance 
        for i in range(len(com)):
            x1, x2 = com[i][0][0], com[i][1][0]
            y1, y2 = com[i][0][1], com[i][1][1]
        
            dis = abs(x1 - x2) + abs(y1 - y2)
        
            if dis <= 2:
                if x1 == x2 and place[x1][max(y1, y2) - 1] == "X":
                    continue
                elif y1 == y2 and place[max(x1, x2) - 1][y1] == "X":
                    continue
                elif abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
                    if place[x1][y2] == "X" and place[x2][y1] == "X":
                        continue
                    
                safe = 0
                break
        
        answer.append(safe)
        
    return answer
