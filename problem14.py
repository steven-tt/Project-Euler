import time
def mything(upper):
    start = time.time()
    mem = {}
    max = (0,0)
    for i in range(2, upper):
        if i in mem:
            continue
        num = i
        mem[i] = 1
        while num != 1:
            if num % 2 == 0:
                num = int(num/2)
            else:
                num = 3 * num + 1
            if num in mem:
                mem[i] = mem[i] + mem[num]
                break
            mem[i] += 1
        if mem[i] > max[1]:
            max = (i,mem[i])
    return max, time.time()-start

mything(1000000)

ls = []
for i in range(0,100000000,1000):
    ls.append((mything(i)[1], i))
ls




#### SOome one elses running against mine
#### http://code.jasonbhill.com/c/project-euler-problem-14/
def histhing():
    start = time.time()

    limit = 1000000
    collatz_length = [0] * limit
    collatz_length[1] = 1
    max_length = [1,1]

    for i in range(1,1000000):
        n,s = i,0
        TO_ADD = [] # collatz_length not yet known
        while n > limit - 1 or collatz_length[n] < 1:
            TO_ADD.append(n)
            if n % 2 == 0: n = int(n/2)
            else: n = 3*n + 1
            s += 1
        # collatz_length now known from previous calculations
        p = collatz_length[n]
        for j in range(s):
            m = TO_ADD[j]
            if m < limit:
                new_length = collatz_length[n] + s - j
                collatz_length[m] = new_length
                if new_length > max_length[1]: max_length = [i,new_length]

    elapsed = (time.time() - start)
    return max_length[0],max_length[1],elapsed

histhing()
