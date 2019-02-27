def is_prime(num):
    if num<=1:
        return False
    if num % 2 == 0 and num > 2:
        return False
    for divisor in range(3, int(num ** (1/2)) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def gen_prime(n):
    '''
    Input: integer
    Like range but only returns primes up to n
    '''
    for i in range(n):
        if is_prime(i):
            yield i

def is_list_prime(ls_int):
    test = True
    for i in ls_int:
        if is_prime(i) == False:
            test = False
            break
    return test
