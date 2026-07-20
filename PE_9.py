"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a = 0
b = 0
c = 0
thousand_list = []
prod_digits = 0
#makes the list of numbers that sums to 1000
for i in range(1, 1000):
    a = i
    for j in range(1, (1000-i)):
        b = j
        c = (1000-i)-j
        thousand_list.append([a,b,c])

for k in range(len(thousand_list)):
    if (thousand_list[k][0]**2) + (thousand_list[k][1]**2) == (thousand_list[k][2]**2):
        prod_digits = thousand_list[k][0] * thousand_list[k][1] * thousand_list[k][2]
    
print(prod_digits)
