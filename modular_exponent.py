from number_theory_functions import extended_gcd, lcm, is_prime, modular_exponent, modular_inverse, gcd

def q2():
    base = 456456 % 1000 # 456
    num1 = 7896543
    num2 = 74365753

    x1 = pow(num1, num2, 1000) # 456^7896543=16
    print(x1)
    
    x2 = pow(base, x1, 1000) # 16^74365753 = 96
    print(x2)

    ans = int(x2 / 100) # 96/100 = 0
    print(f'Q2 ans -> the number is {ans}') # number is zero

def q1():
    # x*911 + 7879*y = 0 (mod 1,000,000)
    d, x, y = extended_gcd(911, 7879)
    # -2733*911 + 316*7879 = 1 -> multiply by 1e6
    # -> ans = (1e6*-2733)*911 + (1e6*316)*7879 

def q4(e,N):
    inverse=[]
    for x in range(2,N-1):
        if gcd(x,N)!=1:
            return False
        for y in inverse:
            if modular_inverse(x,N)==y:
                return False
        inverse.append(modular_inverse(x,N))
    return True

def q4():
    _sols = []
    N = 991
    e = 11
    for x in range(1,N):
        assert modular_exponent(x,e,N) == ((x**e)%991)
        Ex = modular_exponent(x, e, N)
        if Ex == 896:
            print(f'E({x}) = {Ex}')
        _sols.append(Ex)
# E(151) = 896
# E(293) = 896
# E(396) = 896
# E(414) = 896
# E(541) = 896
# E(613) = 896
# E(776) = 896
# E(880) = 896
# E(920) = 896
# E(971) = 896
# E(982) = 896
# לא חחע ולכן לא הפיכה

q2()