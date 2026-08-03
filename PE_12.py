'''
What is the value of the first triangle number to have over five hundred divisors?
'''
import math
#We only need to check half because the evens will have more divisors
trig_list = []
def make_trig(limit):
    trig_list = []
    for i in range(500, limit):
        n_trig = (i/2)*(2 + (i-1))
        trig_list.append(n_trig)
    return trig_list

def check_div(trig_list):
    for num in trig_list:
        count = 0
        for i in range(1, math.floor(num ** 0.5)):
            if num % i == 0:
                count = count + 1
        if count > 250:
            return num

print(check_div(make_trig(50000)))