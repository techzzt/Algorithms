###########################################
#### Topic: 로또의 최고 순위와 최저 순위 ####
# input: lottos                           #
# output: min, max rank                   #
###########################################

# Sleummary: use same numbers in inputs for rank index

def solution(lottos, win_nums):
    answer = []
    lst = []
    lst = [value for value in lottos if value in win_nums]
    n = lottos.count(0)
    rank = [6,5,4,3,2,1]
    rank2 = 0
    if len(lst) == 0 and n == 0:
        rank1, rank2 = 6, 6
    else: 
        rank1 = rank[len(lst)+n-1]
        if len(lst) > 1:
            rank2 = rank[len(lst)-1]
        else:
            rank2 = 6
    answer = [rank1, rank2]
    return answer
