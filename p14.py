def collatz_chain(max):
  longest_chain.max = max
  longest_chain.max_len = 0
  longest_chain(1, 1)
  return longest_chain.max_len

def longest_chain(x, length):
  """Will find longest Collatz sequence by working backwards recursively"""
  if length > 10:
    return
  # base case if number over 1,000,000
  if x > longest_chain.max:
    if length > longest_chain.max_len:
      longest_chain.max_len = length 
    print "hi" + str(x)
    return

  # else send to possible before sequence number
  even_n = x * 2
  odd_n = 0
  if (x -1) % 3 == 0:
    odd_n = (x - 1) / 3
  print even_n
  print odd_n
  if is_even(odd_n) and is_odd(even_n):
    return
  elif odd_n < 1 or is_even(odd_n):
    longest_chain(even_n, length + 1)
  elif even_n > longest_chain.max or is_odd(even_n):
    longest_chain(odd_n, length + 1)
  else:
    longest_chain(even_n, length + 1)
    longest_chain(odd_n, length + 1)

def is_odd(x):
  return (x % 2 != 0)

def is_even(x):
  return (x % 2 == 0)

if __name__ == "__main__":
  print collatz_chain(20)