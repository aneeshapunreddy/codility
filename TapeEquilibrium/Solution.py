  # you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    part_one = A[0]
    part_two = sum(A[1:])
    min_diff = abs(part_one - part_two)
    print min_diff
    
    for i in range (1, len(A)-1):
        part_one += A[i]
        part_two -= A[i]
        
        if abs(part_one - part_two) < min_diff:
            min_diff = abs(part_one - part_two)
    
    print min_diff    
    return min_diff        
