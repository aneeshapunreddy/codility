# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7 
    #counter array for storing all the numbers we encounter
    counter = [False]*(len(A)+1)
    
    # iterate through each element in A
    # if a number occurs, it's position - 1 th element will be equal to that number in the counter array
    for element in A:
        if 1 <= element <= (len(A)+1):
            counter[element-1] = True 
    
    for index in xrange(len(A)+1):
        if counter[index] == False:
            return  index + 1
            
    raise Exception("Should never be here")
    return -1
