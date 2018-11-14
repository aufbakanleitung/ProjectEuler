"""
Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def isPandigital(n):
    testString = str(n)
    numberlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in testString:
        try:
            numberlist.remove(int(a))
        except ValueError:
            break
        # print(numberlist)
        if numberlist == []:
            # print("it's pandigital")
            return True
    # print("this is not pandigital")
    return False

from itertools import permutations

def is_rule_abiding(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    nstr = str(n)
    counter = 0
    for a in range(1,8):
        testnr = int(nstr[a] + nstr[a+1] + nstr[a+2])
        if testnr % divisors[a-1] == 0:
            # print(testnr, "is divisible by", divisors[a-1])
            counter += 1
    return counter == 7

tuple_sum = 0
for permutation_tuple in permutations(range(10)):
    perm_str = ''.join([str(x) for x in permutation_tuple])
    if is_rule_abiding(perm_str):
        tuple_sum += int(perm_str)

print(tuple_sum)