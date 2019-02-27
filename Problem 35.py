import time

import common_functions as cf

def rotate(num_int):
    '''

    '''
    # Workd for three digit numbers unsure how to do an finite sum inside list comprehension
    # list_of_rotate = [str(num_int)[i] + str(num_int)[(i+1)%3] + str(num_int)[(i+2)%3] for i in range(len(str(num_int)))]
    num_str = str(num_int)
    num_len = len(num_str)
    ls_of_rot = []
    for i in range(num_len):
        new_num_str = ''
        for j in range(num_len):
            new_num_str += num_str[(i+j)%num_len]
        ls_of_rot.append(new_num_str)
    for i in range(num_len):
        ls_of_rot[i] = int(ls_of_rot[i])
    return ls_of_rot

count = 0
for i in cf.gen_prime(1000000):
    if cf.is_list_prime(rotate(i)):
        count += 1
print(count)
