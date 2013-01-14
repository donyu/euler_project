def sum_mult(x, y):
    sum = 0
    for i in xrange(1000):
        if i % x == 0 or i % y == 0:
            sum += i
    return sum

def sum_mult_opt(x, y):
    return sum_divisible(x) + sum_divisible(y) - sum_divisible(x*y)

def sum_divisible(x):
    p = 999 / x 
    return x * (p * (p+1)) / 2

print sum_mult(3, 5)
print sum_mult_opt(3, 5)
