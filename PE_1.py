"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def PE_1_three_loops():
    ''' Project Euler Problem 1: Multiples of 3 and 5 with 3 loops'''
    sum = 0
    for i in range(15, 1000, 15):
        sum = sum -i
    for i in range(3, 1000, 3):
        sum = sum + i
    for i in range(5, 1000, 5):
        sum = sum + i
    return sum

def PE_1_two_loops():
    ''' Project Euler Problem 1: Multiples of 3 and 5 with 2 loops'''
    sum = 0
    for i in range(1000):
        if i % 3 ==0:
            sum = sum + i
    
    for i in range(1000):
        if i % 5 ==0 and i % 15 != 0:
            sum = sum+i
    return sum

def PE_1_one_loop():
    ''' Project Euler Problem 1: Multiples of 3 and 5 with 1 loop'''
    sum = 0
    for i in range(1000):
        if i % 15 == 0:
            sum = sum + i
        elif i % 5 == 0:
            sum = sum + i
        elif i % 3 == 0:
            sum = sum + i
    return sum

def PE_1_list_comprehension():
    ''' Project Euler Problem 1: Multiples of 3 and 5 with list comprehension'''
    total = sum([i for i in range(1000) if i % 5 == 0 or i % 3 == 0])
    return total
if __name__ == "__main__":
    print("Three Loops: ", PE_1_three_loops())
    print("Two Loops: ", PE_1_two_loops())
    print("One Loop: ", PE_1_one_loop())
    print("List Comprehension: ", PE_1_list_comprehension())

    ## YOUR CODE GOES HERE