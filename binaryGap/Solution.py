def solution(N):
    # write your code in Python 2.7
    max_count = 0
    current_gap = 0
    
    #to avoid tailing zeros
    while N>0 and N%2==0:
        N //= 2
    
    while N>0:
        remainder = N%2
        if remainder == 0:
            current_gap +=1
        else:
            if current_gap !=0:
                max_count = max(max_count, current_gap)
                current_gap = 0
        N //=2
    return max_count 
