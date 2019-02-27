def sep_int(integer):
    '''
    Takes an integer and splits its digits into a list
    '''
    seperated_int = []
    for i in str(integer):
        seperated_int.append(int(i))
    return seperated_int
# O(n)

def is_prime(num):
    if num<=1:
        return False
    if num % 2 == 0 and num > 2:
        return False
    for divisor in range(3, int(num ** (1/2)) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def permute(lst):
    lst_nums = [0] * 
