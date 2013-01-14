def prime_factors(n):
  """Returns all prime factors of a positive integer"""
  factors = []
  d = 2
  while n > 1:
    while n%d == 0:
      factors.append(d)
      n /= d
    d += 1
    if d * d > n:
      if n > 1:
        factors.append(n)
      break

  return factors

def largest_prime_factor(x):
  p_factors = prime_factors(x)
  p_factors.sort()
  return p_factors[-1]

if __name__ == "__main__":
  print largest_prime_factor(600851475143)
