
def solution(A):
    # write your code in Python 2.7
    if len(A)==0:
        distinct = 0
    else:
        distinct = 1
    A.sort()
    
    for index in xrange(1, len(A)):
        if A[index] == A[index-1]:
            #it's the same element
            continue 
        else:
            distinct +=1
            
    return distinct        
