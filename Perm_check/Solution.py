def solution(A):
    # write your code in Python 2.7
    #create an array to keep a track of the numbers
    tracking_array = [-1]*len(A)
    
     #variable to keep a check on numbers
    limit = len(A)
    
    for element in A:
        # if the number is greater than the limit, it's not a permutation
        if not 1 <= element <= limit:
            return 0
        else:
            # condition to check if a number appeared in the list twice
            if tracking_array[element-1] != -1:
                return 0
            #condition to check the first occurance of a number
            else:
                tracking_array[element-1] = 1    
    #if both the if conditions fail, it's a permutation    
    return 1
