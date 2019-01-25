import time
def is_prime(num):
    if num<=1:
        return False
    if num % 2 == 0 and num > 2:
        return False
    for divisor in range(3, int(num ** (1/2)) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def consect_prime(lim):

    max_len = 0
    num = 0
    for i in range(lim):
        if is_prime(i):
            #print(i)
            sum = 0
            sum_len = 0
            for j in range(i,lim):
                if is_prime(j):
                    # print(j)
                    sum += j
                    sum_len += 1
                    if sum >= lim:
                        break
                    elif is_prime(sum) and sum_len > max_len:
                        #print(sum,sum_len)
                        num = sum
                        max_len = sum_len

    return num

start = time.time()
consect_prime(1000000)
print(time.time()-start)
