from math import sqrt

def pyth_triplet(sum):
  nums = [i**2 for i in xrange(1, sum)]
  for k in xrange(len(nums) - 1, -1, -1):
    i = 0
    j = k - 1
    while i < j:
      if (nums[i] + nums[j] == nums[k]) and (sqrt(nums[i]) + sqrt(nums[j]) + sqrt(nums[k]) == sum):
        return sqrt(nums[j]) * sqrt(nums[i]) * sqrt(nums[k])
      if (nums[i] + nums[j]) > nums[k]:
        j -= 1
      else: 
        i += 1
  return -1

def main():
  print pyth_triplet(1000)

if __name__ == "__main__":
  main()
