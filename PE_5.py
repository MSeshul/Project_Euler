import math
n = 20
factor_list = []
#We need to find the prime factorization of each number
def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

lower_bound = math.ceil(n**0.5)
for number in range(lower_bound, (n+1)):
   if (number ** 0.5) % 1 == 0:
        factor_list.append(number)
   else:
        prime = check_prime(number)
        if prime == True:
            factor_list.append(number)

total = 1
for factor in factor_list:
    total = total * factor

print(total)