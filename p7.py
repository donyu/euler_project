def nth_prime(n):
  if n == 1:
    return 2
  start = 3
  primes = [2]
  prime_nth = 1
  while prime_nth < n:
    if is_prime(start, primes):
      primes.append(start)
      prime_nth += 1
    start += 1
  return primes[-1]

def is_prime(x, primes):
  for p in primes:
    if x % p == 0:
      return False
  return True

if __name__ == "__main__":
  print nth_prime(10001)

