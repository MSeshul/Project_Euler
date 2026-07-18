import math
def check_prime(number):
    for i in range(2, math.ceil(number**0.5)+1):
        if number % i == 0:
            return False
    return True

nth_prime = 10001
prime_list = [2]

def primes():
    for number in range(3, 10000000000, 2):
        n = prime_list[-1]
        if len(prime_list) > nth_prime-1:
            return n
        prime = check_prime(number)
        if prime == True:
            prime_list.append(number)

print(primes())