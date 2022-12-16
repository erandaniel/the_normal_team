from random import randrange
from math import pow
def lcm(a,b):
    return ((a*b)/gcd(a,b))

def prime_fators(n):
    result = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            if (is_prime(i)):
                result.append(i)
            n //= i
            i += 1
    print(result)
    return result

def gcd(a,b):
    if (a == 0):
        return b
    if (b == 0):
        return a

    # base case
    if (a == b):
        return a

    # a is greater
    if (a > b):
        return gcd(a%b, b)
    return gcd(a, b%a)

"""
Returns the extended gcd of a and b

Parameters
----------
a : Input data.
b : Input data.
Returns
-------
(d, x, y): d = gcd(a,b) = a*x + b*y
"""
def extended_gcd(a,b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    return gcd, y, x - y * (a // b)

    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    """
    if(a%n == 1):
        return 1
    
    
    """
def modular_inverse(a,n):
    if gcd(a,n)==1:
        return 0
    return pow(a, n-2, n)

def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    return pow(a, d, n)
    
    # sum = 1
    # d = bin(d)
    # d = d[::-1]
    # for i in range(len(d)):
    #     if d[i] == 'b': #0b010101 ->10010100b b is the end
    #         return sum % n
    #     if d[i] == '1':
    #         sum *= (a ** (2**i) % n)


def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None