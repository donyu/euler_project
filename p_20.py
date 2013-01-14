import math

def sum_digits(x):
    factorial = math.factorial(x)
    sum = 0
    for d in str(factorial):
        sum += int(d)
    return sum

if __name__ == "__main__":
    print sum_digits(100)
