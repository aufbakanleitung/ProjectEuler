"""

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
from math import sqrt, isclose
import csv


# Triangular root formula for triangle test
def isTriangle(n):
    tn = ((sqrt(8*n + 1)) - 1) / 2
    if isclose(tn, round(tn)):
        return True
    else:
        return False


def word2numberConverter(data):
    triangleWordSum = 0
    for row in data:
        for word in row:
            wordvalue = 0
            for letter in word:
                wordvalue += ord(letter)-64
            if isTriangle(wordvalue):
                triangleWordSum += 1
                print(word + " = " + str(wordvalue) + " is " + str(isTriangle(wordvalue)))
    print(triangleWordSum)


with open('p042_words.txt' ,'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    word2numberConverter(data)


def triangleGenerator(n):
    trianglelist = []
    for a in range(0, n):
        trianglelist.append(int(0.5 * a * (a+1)))
    return trianglelist

