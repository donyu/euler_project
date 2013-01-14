import sys

def sum_file(input):
    sum = 0
    for number in input:
        sum += long(number)
    return str(sum)[0:10]

if __name__ == "__main__":
    input_file = file(sys.argv[1], 'r')
    print sum_file(input_file)
