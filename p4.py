def largest_palindrome(x):
	max_args = (100, 100)
	max_val = 0
	for i in xrange(100, 1000):
		for j in xrange(100, 1000):
			val = i * j
			if is_palindrome(val) and val > max_val:
				max_args = (i, j)	
				max_val = val
	return max_val

def is_palindrome(num):
	num = str(num)
	if num[:] == num[-1::-1]:
		return True
	return False	

def main():
	print "The largest palindrome from product of two 3-digit numbers is: %d" % (largest_palindrome(3))

if __name__ == "__main__":
	main()
