def sum_digits(x):
    power = 2**x
    sum = 0
    for d in str(power):
        sum += int(d)
    return sum

if __name__ == "__main__":
    print sum_digits(1000)
