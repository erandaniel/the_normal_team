import number_theory_functions
import rsa_functions
from random import randrange

def q1():
    # x*911 + 7879*y = 0 (mod 1,000,000)
    d, x, y = extended_gcd(911, 7879)
    # -2733*911 + 316*7879 = 1 -> multiply by 1e6
    # -> ans = (1e6*-2733)*911 + (1e6*316)*7879 

def q4(e,N):
    inverse=[]
    for x in range(2,N-1):
        if number_theory_functions.gcd(x,N)!=1:
            return False
        for y in inverse:
            if number_theory_functions.modular_inverse(x,N)==y:
                return False
        inverse.append(number_theory_functions.modular_inverse(x,N))
    return True

def q5(p,q,m):
    print(p)
    print(q)
    print(m)
    print("-----------")
    N = p*q
    phi = (p-1)*(q-1)
    for i in range(N):
            e = randrange(1, phi - 1)
            d = number_theory_functions.modular_inverse(e,phi)
            if(d != 0):
                break
    print(e)
    print(d)
    test = rsa_functions.RSA((N,d),(N,e))
    c = test.encrypt(m)
    print(str(test.decrypt(c)))
    return c


