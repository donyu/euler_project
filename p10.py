from primes import fast_primes

def main():
  prime_sum = fast_primes(2e6)
  print sum(prime_sum) + 2

if __name__ == "__main__":
  main()
