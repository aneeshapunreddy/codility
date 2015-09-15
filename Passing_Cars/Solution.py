
def solution(A):
    # write your code in Python 2.7
    pass_count = 0
    sum_array = sum(A)
    
    for element in A:
        if element == 0:
            pass_count += sum_array
        elif element == 1:
            sum_array -= 1
    if pass_count <= 1000000000:        
        return pass_count 
    else:
        return -1 
