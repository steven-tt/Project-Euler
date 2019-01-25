# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math
def num_split(num):
    '''
    Input: Integer
    Output: The sum of the factorial of each digit in the input integer
    '''
    sum = 0
    for i in str(num):
        sum += math.factorial(int(i))
    return sum

curious = 0
for i in range(math.factorial(9)*7):
    if i == num_split(i):
        # print(i,num_split(i))
        curious += num_split(i)
print(curious)

# math.factorial(9)*7
# This is an upperbound becasue if we had a 7 digit number of all nines and did the num split
# the resulting number is seven digits. If we do it with eight 9's we still get a seven digit number.
# I orginal just kept guessing higher and higher numbers until I read someone elses blog
# After getting the right answer
