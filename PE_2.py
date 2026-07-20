"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms. (In this case the sequence only starts with a single 1)
"""
import math, time

def sum_even_fib_terms(limit: int) -> int:
    """
    Calculates the sum of even Fibonacci numbers up to a given limit.

    Args:
        limit (int): The upper limit for Fibonacci numbers.

    Returns:
        int: The sum of even Fibonacci numbers up to the limit.
    
    Examples:
    >>> sum_even_fib_terms(10)
    10
    >>> sum_even_fib_terms(1)
    0
    >>> sum_even_fib_terms(100)
    44
    >>> sum_even_fib_terms(-2)
    0
    """
    fib_list = [1,2]
    while fib_list[-1] < limit:
        fib_list.append(fib_list[-1]+fib_list[-2])
    even_sum = 0
    for i in range(len(fib_list)):
        if limit < 2:
            even_sum = 0
        elif fib_list[i] % 2 == 0:
            even_sum = even_sum + fib_list[i]

    return even_sum
    even_sum = 0
    x = (1+(5 ** 0.5))/2
    y = (1-(5 ** 0.5))/2
    for i in range(2, limit, 3):
        even_sum = even_sum + ((x**i)-(y**i))/(5**0.5)
    
    return even_sum
    fib_list = [1,1]
    while fib_list[-1] < 1000:
        fib_list.append(fib_list[-1]+fib_list[-2])
    
        
    
if __name__ == "__main__":
    print("Sum of even Fibonacci numbers up to 4 million: ", sum_even_fib_terms(4000000))
    
fibs_list = [1,1]
while fibs_list[-1] < 1000:
    fibs_list.append(fibs_list[-1]+fibs_list[-2])
print(fibs_list[-1])
print(len(fibs_list))

p = (1+(5 ** 0.5))/2
q = (1-(5 ** 0.5))/2
fib_number = 0
while fib_number < (10**10):
    i = 0
    fib_number = ((p**i)+(q**i))/(5**0.5)
    i = i+1
print(fib_number)