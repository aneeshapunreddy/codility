def solution(S):
    if len(S)%2 == 0:
        return -1
    else:
        mid = len(S)//2
        begin = 0
        end = len(S)-1
            
        while begin<mid:
            if S[begin]!= S[end]:
                return -1 
            begin +=1
            end -=1
        return mid 
