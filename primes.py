import numpy

def fast_primes(n):
  """Uses fast code to return array of primes"""
  sieve = numpy.ones(n/2, dtype=numpy.bool)
  for i in xrange(3, int(n**0.5) + 1, 2):
    if sieve[i/2]:
      sieve[i*i/2::i] = False
  return 2*numpy.nonzero(sieve)[0][1::]+1

def nth_prime(n):
  """Get the nth prime number"""
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

def get_primes(n, sum = False):
  """Get all prime numbers below number n"""
  num = 2
  primes = []
  tot_sum = 0
  while num < n:
    if is_prime(num, primes):
      if sum:
        tot_sum += num
      primes.append(num)
    num += 1
  if sum:
    return tot_sum
  return primes

def is_prime(x, primes):
  """Check if a number is prime given number and lower prime #s"""
  for p in primes:
    if x % p == 0:
      return False
  return True

