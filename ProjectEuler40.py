"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

d = ''

for a in range(1,1000001):
    d += str(a)
print(d)
print(d[0],d[9],d[99],d[999],d[9999],d[99999],d[999999])
print(int(d[0]) * d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999])