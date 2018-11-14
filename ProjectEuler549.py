import timeit

def primeList(n): #primesieve: returns list of primes
    nroot = int(n**0.5)+1
    sieve = list(range(n+1))
    sieve[1] = 0
    
    for i in range(2, nroot):
        if sieve[i] != 0:
            m = int(n/i - i)
            sieve[i*i: n+1:i] = [0] * (m+1)
    sieve = [x for x in sieve if x !=0]
    return sieve

from math import *; from itertools import count, islice

def isPrime(n): #test if number is prime
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
#     n=6516686
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1

    return factors
# print(str(timeit.timeit(prime_factors, number=10)))
# print(prime_factors())

def metafactorial():
    n=312507
    primelist = []
    tester = prime_factors(n)
    
    for teller in range(2,n+1):
        for deler in prime_factors(teller):
#             print(teller)
            if deler in tester:
                tester.remove(deler)
            if tester == []:
                return teller
# print(metafactorial(108))

def metafactorial2(n):
#     n=312507
    for teller in range(2,n+1):
        for deler in prime_factors(teller):
#             print(str(n) + " / " + str(deler) + " (" + str(teller) + ")")
            if n % deler == 0:
                if n == deler:
                    return teller
                else:
                    n //= deler
# print(metafactorial2(12))
# print(str(timeit.timeit(metafactorial2, number=10)))

def Euler549(n): #Divisibility of factorials
    for teller in range(1,n+1):
#         print(factorial(teller))
        if factorial(teller) % n == 0: #true if divisible
            return teller
# print(Euler549(10))
S=3000
def Euler549add(S): #Sum of Divisibility of factorials 
    sum = 0
    for teller in range(2,S+1):
        if isPrime(teller):
            sum += teller
        else:
#             if not metafactorial(teller) == metafactorial2(teller):
#                 print(str(teller) + " geeft: " + str(metafactorial(teller)) + " of " + str(metafactorial2(teller)))
            sum += metafactorial2(teller)
    return sum
# print(Euler549add())
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("Euler549add(S)", setup="from __main__ import Euler549add, S",number=1))

