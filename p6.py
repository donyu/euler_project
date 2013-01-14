def sum_squares(x):
  """sum the squares up to number x"""
  total = 0
  for i in xrange(1, x+1):
    total += i**2
  return total

def square_sum(x):
  """square the sum of numbers up to x"""
  sum_total = 0
  for i in xrange(1, x+1):
    sum_total += i
  return sum_total**2

def main():
  print abs(sum_squares(100) - square_sum(100))

if __name__ == "__main__":
  main()

