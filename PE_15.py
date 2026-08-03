'''
Starting in the top left corner of a 2 x 2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many routes for a 20 x 20 grid?
'''
import math
#We can rewrite this problems similarly to pascals triangle. 
#The middle term would be 21 choose 10
#thanks combo class
grid_size = 20
pascals_row = grid_size * 2
routes = math.comb(pascals_row, (math.ceil(pascals_row/2)))
print(routes)