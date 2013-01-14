from math import sqrt

def fib(n):
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n*sqrt(5)))

def fib_even_sum(num_max):
    n = 2
    sum = 0
    while fib(n) < num_max:
        if fib(n) % 2 == 0:
            sum += fib(n)
        n += 1
    return sum
    
if __name__ == "__main__":
    print fib_even_sum(4000000)
