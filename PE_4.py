palindrome_list = []
def products():
    for j in range(999, 800, -1):
        n2 = j
        for i in range(999, 800, -1):
            n1 = i
            product1 = (n1*n2)
            reverse = int(str(product1)[::-1])
            if product1 == reverse:
                palindrome_list.append(product1)

products()
print(max(palindrome_list))
