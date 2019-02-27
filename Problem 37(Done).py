import time

def is_prime(num):
    '''
    input: integer
    output: boolean
    Takes a number and brute force tests if it is prime.
    Note: For a much quicker, but not selfmade use the isprime() test from sympy
    '''
    if num<=1:
        return False
    if num % 2 == 0 and num > 2:
        return False
    for divisor in range(3, int(num ** (1/2)) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def trunc(num):
    '''
    Input: integer
    Output: boolean
    Takes in an integer and left and right truncates it eg right 3797,379,37,3,
    and tests to see if all the numbers are prime.
    '''
    # This is the left and right truncations done using list comprehension got really ugly
    #[int(str(num)[0:len(str(num))-i]) for i in range(len(str(num)))] + [int(str(num)[i:len(str(num))]) for i in range(len(str(num)))]
    num = str(num)
    list_nums = []
    #Does left and right truncations and adds them to list
    for i in range(len(num)):
        list_nums.append(num[:len(num)-i])
        list_nums.append(num[i:len(num)])
    #Turns all the nums to integers
    for i in range(len(list_nums)):
        list_nums[i] = int(list_nums[i])
    #Return the unique objects in the list
    return set(list_nums)

def is_prime_trunc(num):
    '''
    Input:integer
    Output: boolean
    Takes in an integer and returns true if all of the truncated numbers are prime.
    '''
    list = trunc(num)
    for i in list:
        if is_prime(i) == False:
            return False
            break
    return True

def sum_tunc_primes():
    prime_count, it_count, sum, start = 0, 10, 0, time.time()
    while prime_count < 11:
        if is_prime_trunc(it_count):
            prime_count += 1
            sum += it_count
        it_count += 1
    return sum, time.time()-start

sum_tunc_primes()
