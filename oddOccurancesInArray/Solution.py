def solution(A):
    # write your code in Python 2.7
    result = 0
    for element in A:
        result ^=element
    return result  
