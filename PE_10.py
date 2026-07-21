"""
Find the sum of all the primes below two million.
"""
#This is very similar to previous questions
import math
prime_list = [2]
n = 3
total = 0

#input n output bool
def check_prime(n):
    for i in range(2, math.ceil(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes():
    for j in range(100000):
        for n in range((j*1000)+3, 1000+(j*1000)+3, 2):
            if check_prime(n) == True:
                prime_list.append(n)
        if prime_list[-1] > 2000000:
            return prime_list
#Primes will find the correct thousand that the highest is in

#We have to remove the ones higher than 2 million
prime_list = primes()
for number in range(2000):
    if prime_list[-1] > 2000000:
        prime_list.pop(-1)
        
prime_set = set(prime_list)
print(sum(prime_set))