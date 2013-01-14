from math import sqrt

def is_prime(x):
    for i in xrange(2, int(sqrt(x))):
        if x % i == 0:
            return False
    return True

def largest_prime_factor(x):
    max_prime = 2  
    for i in xrange(2, x):
        if x % i == 0 and is_prime(i):
            max_prime = i
    return max_prime

if __name__ == "__main__":
    print largest_prime_factor(600851475143)
