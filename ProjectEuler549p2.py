import matplotlib.pyplot as plt
import random
import timeit
from matplotlib.pyplot import grid
from root.PE14 import teller
def primesbelow(N):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    #""" Input N>=6, Returns a list of primes, 2 <= p < N """
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    sieve = [True] * (N // 3)
    sieve[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000

def isprime(n, precision=7):
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
    if n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n <= 3:
        return n >= 2
    elif n % 2 == 0:
        return False
    elif n < _smallprimeset:
        return n in smallprimeset


    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1: continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1: return False
            if x == n - 1: break
        else: return False

    return True

# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3

    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g==1:
            ys = y
            for i in range(min(m, r-k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g
smallprimes = primesbelow(1000) # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000

def primefactors(n, sort=False):
    factors = []

    for checker in smallprimes:
        while n % checker == 0:
            factors.append(checker)
            n //= checker
        if checker > n: break

    if n < 2: return factors

    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
        factors.extend(primefactors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()

    return factors
def factorization(n):
    factors = {}
    for p1 in primefactors(n):
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors


def metafactorial2(n): #s(n) be the smallest number m such that n divides m!.
#     n=312507
    for teller in range(2,n+1):
        for deler in primefactors(teller):
#             print(str(n) + " / " + str(deler) + " (" + str(teller) + ")")
            if n % deler == 0:
                if n == deler:
                    return teller
                else:
                    n //= deler
# print(str(timeit.timeit(metafactorial2, number=10)))

def mf2patterntest(n):
    mf2 = 0
    mf3 = []
    for teller in range(2,n):
        mf2 = (metafactorial2(teller))
        if mf2 == teller/2:
            mf3.append(teller)
    plt.plot(mf3)
    grid('on')
    plt.ylabel('y(x) is the smallest number m such that x divides m!')
    plt.figure(num=1,figsize=(30,15))
    plt.show()
    return mf3
# mf2patterntest(2000)

def Euler549add(S): #Sum of Divisibility of factorials 
    Ssum = 0
    for teller in range(2,S+1):
        if isprime(teller):
            Ssum += teller
        else:
#             if not metafactorial(teller) == metafactorial2(teller):
#                 print(str(teller) + " geeft: " + str(metafactorial(teller)) + " of " + str(metafactorial2(teller)))
            Ssum += metafactorial2(teller)
    return Ssum
#print(Euler549add(100))

def fileIt(n):
    f = open("Euler549-2.txt","a")
    for teller in range(1,n):
        mf2 = metafactorial2(teller)
        f.write(str(mf2) + "\n")
    f.close()
    return "Done"
# plotIt(1000)

def plotIt(n):
    plotList = [0]
    for teller in range(1,n):
        if isprime(teller):
            plotList.append(0)
        else:
            plotList.append(metafactorial2(teller))
    plt.plot(plotList)
    grid('on')
    plt.ylabel('y(x) is the smallest number m such that x divides m!')
    plt.figure(num=1,figsize=(30,15))
    plt.show()    
# plotIt(200)

# """time it"""
# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("Euler549add(2000)", setup="from __main__ import Euler549add",number=1))

totients = {}
def totient(n):
    if n == 0: return 1s

    try: return totients[n]
    except KeyError: pass

    tot = 1
    for p, exp in factorization(n).items():
        tot *= (p - 1)  *  p ** (exp - 1)

    totients[n] = tot
    return tot

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return abs((a // gcd(a, b)) * b)