import sys

def get_digits(file):
  return ''.join([line.strip() for line in file])

def main(file):
  digits= get_digits(file)
  beg = 0
  end = 5
  max_prod = 0
  while end < len(digits):
    product = prod_digits(digits[beg:end])
    if product > max_prod:
      max_prod = product
    beg += 1
    end += 1
  return max_prod

def prod_digits(digits):
  prod = 1
  for d in digits:
    prod *= int(d)
  return prod

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Need another argument for digits file"
    exit(0)
  print main(file(sys.argv[1], 'r'))
