n = 0
m = 0
for i in range(101):
    n = n + (i**2)
    m = m + i

square = m ** 2
print(square - n)