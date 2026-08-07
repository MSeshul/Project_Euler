'''What is the sum of the digits of the number 2^1000?'''
num = 2 ** 1000
sum = 0
num_list = list(map(int, str(num)))
for i in num_list:
    sum = sum + i
print(sum)