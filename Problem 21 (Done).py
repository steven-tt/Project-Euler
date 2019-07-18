# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def sum_proper(n):
    '''
    O(logn)?
    Input: integer
    Output: integer
    Takes the all divisors (except itself) of the inut number and outputs the sum of the lst_of_divisors
    '''
    lst_of_divisors = [1]
    for i in range(2, round(n**(1/2))):
        if n % i == 0:
            lst_of_divisors.append(i)
            lst_of_divisors.append(int(n/i))
    # print(lst_of_divisors)
    return sum(lst_of_divisors)

sum_proper(220)
sum_proper(284)

dict_of_amicable_numbers = {}
for i in range(10001):
    a, b = sum_proper(i), sum_proper(sum_proper(i))
    if str(i) in dict_of_amicable_numbers:
        continue
    elif i == a:
        continue
    elif i == b:
        dict_of_amicable_numbers[str(i)] = a
        dict_of_amicable_numbers[str(a)] = i

dict_of_amicable_numbers

int_sum_of_amicable_numbers = 0
for i in dict_of_amicable_numbers:
    int_sum_of_amicable_numbers += int(i)
int_sum_of_amicable_numbers
