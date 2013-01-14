def factors_count(x):
  count = 0
  for i in xrange(1, x + 1):
    if x % i == 0:
      count += 1
  return count

def max_divisible_num(max):
  tri_num = 1
  i = 2
  while factors_count(tri_num) < max:
    tri_num += i
    i += 1
  return tri_num

if __name__ == "__main__":
  print max_divisible_num(500)
