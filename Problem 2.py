import time
def fib_even_limit(lim):
    '''
    Input: limit
    Return: sum, time elapsed to run function
    This function sums the even valued fibonacci numbers less than the limit.
    It runs really fast even for large limits.
    I am pretty sure this is becasue it is just doing arithmetic with integers,
    however I am unsure.
    I could not get the funtion to show more than 0.0 seconds
    '''
    start = time.time()
    a,b,sum = 1,2,0
    while a < lim:
        if a % 2 == 0:
            sum += a
        a,b = b,a+b
    return sum,time.time()-start

fib_even_limit(4000000)
