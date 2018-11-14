"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""
from math import *; from itertools import count, islice

def isPrime(n):  # test if number is prime
    if n == 1:
        return False
    for a in range(2,int(sqrt(float(n))) + 1):
        if n%a == 0:
            return False
    return True

print(isPrime(1))

truncatable_list = []
truncatable_sum = 0

def truncatable(n):
    len_n = len(str(n))
    maxlen = (2*len_n) - 1

    truncList = []l;
    for a in range(1, len_n):
        # print(str(n)[0:a])
        if isPrime(int((str(n)[0:a]))):
            truncList.append(str(n)[0:a])

    for a in range(0, len_n):
        # print(str(n)[a:len_n])
        if isPrime(int(str(n)[a:len_n])):
            truncList.append(str(n)[a:len_n])

    if len(truncList) == maxlen:
        print(truncList)
        truncatable_list.append(truncList)
        global truncatable_sum
        truncatable_sum += n
        return True
    return False

def problem37(t_range):
    for a in range(10,t_range):
        truncatable(a)
    print(truncatable_list)
    print(truncatable_sum)

problem37(1000000)


