'''Find the sum of the digits in the number 100!.'''
import math
number = math.factorial(100)
digits = list(map(int, str(number)))
print(sum(digits))