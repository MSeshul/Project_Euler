import math

def get_factors(n: int) -> list[int]:
    """
    Returns a sorted list of all unique factors of a given positive integer.

    Args:
        n (int): The integer to find factors for.

    Returns:
        list[int]: A sorted list of factors of n.

    Examples:
    >>> get_factors(25)
    [1, 5, 25]
    >>> get_factors(12)
    [1, 2, 3, 4, 6, 12]
    >>> get_factors(1)
    [1]
    >>> get_factors(-2)
    []
    """
    factor_list = []
    for i in range(1, math.ceil(n**0.5)+1):
        if n % i == 0:
            factor_list.append(i)
    for i in range(len(factor_list)):
        factor_list.append(n/factor_list[i])

    return factor_list

def is_prime(n: int) -> bool:
    """
    Determines whether a given integer is a prime number.

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.

    Examples:
    >>> is_prime(17)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    factors_number = len(get_factors(n))
    if factors_number <= 2:
        return True
    else:
        return False
    
    

def largest_prime_factor(n: int) -> int:
    """
    Finds the largest prime factor of a given integer.

    Args:
        n (int): The integer to find the largest prime factor for.

    Returns:
        int: The largest prime factor of n, or 0 if n <= 1.

    Examples:
    >>> largest_prime_factor(35)
    7
    >>> largest_prime_factor(12)
    3
    >>> largest_prime_factor(1)
    0
    """
    factor_list = get_factors(n)
    prime_list = []
    for i in factor_list:
        if is_prime(i) == True:
            prime_list.append(i)
    
    return prime_list[-1]


if __name__ == "__main__":
    print("get_factors(25): ", get_factors(25))
    print("is_prime(17): ", is_prime(17))
    print("largest_prime_factor(90005673681): ", largest_prime_factor(90005673681)) #should return 1109
    #600851475143