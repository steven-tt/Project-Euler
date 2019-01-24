import time
def sum_35_below(lim):
    '''
    Input: upper limit
    Output: sum, elapsed time
    Takes the sum of multiples of 3 and 5 less than the limit and sums them
    '''
    start = time.time()
    sum = 0
    for i in range(lim):
        if i % 3 == 0 or i % 5 == 0:
            sum +=i
    return sum, time.time()-start

sum_35_below(1000)
