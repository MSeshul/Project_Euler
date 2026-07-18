import math

def PE_0():
    sum = 0
    for i in range(1, 153000, 2):
        square = i**2
        sum = sum + square
    return sum

if __name__ == "__main__":
    print(PE_0())
