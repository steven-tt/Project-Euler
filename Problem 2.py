def fib_even_limit(lim):
    a,b,sum = 1,2,0
    while a < lim:
        if a % 2 == 0:
            sum += a
        a,b = b,a+b
    return sum

fib_even_limit(40000000)
