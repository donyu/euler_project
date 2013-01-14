def smallest_mult(x):
  # find maximum smallest multiple
  max = 2
  for i in xrange(3, x+1):
    if max % i != 0:
      for j in lcm(i):
        max *= j
  return max

def lcm(x):
  ret_val = [x]
  for i in xrange(2, x+1):
    if x % i == 0 and int(x / i) > 1:
      ret_val.append(int(x / i))
      del ret_val[0]
  return ret_val

def main():
  print smallest_mult(20)

if __name__ == "__main__":
  main()
