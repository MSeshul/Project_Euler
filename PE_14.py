x = 0
longest = 0
for i in range(3, 1000000):
    count = 0 
    number = i
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            count = count + 1
        else:
            number = (3 * number ) + 1
            count = count + 1
    if count > longest:
        x = i
        longest = count
print(x)



    

