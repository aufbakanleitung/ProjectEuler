"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?"""
from math import sqrt, isclose
from collections import Counter

perimeterList = []

for a in range(1,999):
    for b in range(1,999):
        hypo = sqrt(a * a + b * b)
        if isclose(hypo, int(hypo)):
            perimeter = a + b + int(hypo)
            perimeterList.append(perimeter)

print(Counter(perimeterList))