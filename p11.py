import sys

class ProductGrid():

  def __init__(self, file):
    self.grid = []
    for line in file:
      row = []
      nums = line.strip().split()
      for num in nums:
        row.append(int(num))
      self.grid.append(row)

  def max_prod(self):
    max_prod = 0

    # loop through all possible 4x4 boxes
    for i in xrange(17):
      for j in xrange(17):
        # send this 4x4 box to get_prod function
        prod = self.get_prod(i, j)
        if prod > max_prod:
          max_prod = prod

    return max_prod

  def get_prod(self, top_y, top_x):
    max_prod = 0
    prod = 1
    # go through horizontals
    for i in xrange(4):
      for j in xrange(4):
        prod *= self.grid[top_y + i][top_x + j]
      if prod > max_prod:
        max_prod = prod
      prod = 1

    # go through verticals
    for i in xrange(4):
      for j in xrange(4):
        prod *= self.grid[top_y + j][top_x + i]
        nums.append(self.grid[top_y + j][top_x + i])
      if prod > max_prod:
        max_prod = prod
      prod = 1 

    # go through diagonal #1
    for i in xrange(4):
      prod *= self.grid[top_y + i][top_x + i]
    if prod > max_prod:
      max_prod = prod
    prod = 1

    # go through diagonal #2
    for i in xrange(4):
      prod *= self.grid[top_y + i][top_x + (3 - i)]
    if prod > max_prod:
      max_prod = prod

    return max_prod

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Not enough arguments"
    exit(0)
  input_file = file(sys.argv[1], 'r')
  prod_grid = ProductGrid(input_file)
  print prod_grid.max_prod()


