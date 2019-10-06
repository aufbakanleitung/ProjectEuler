import timeit
from lib2to3.fixer_util import Number
def principal_period(s): #numerical repetition finder 
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

def primeList(n): #primesieve: returns list of primes
    nroot = int(n**0.5)+1
    print(nroot)
    sieve = list(range(n+1))
    sieve[1] = 0
    print(sieve)
    
    for i in range(2, nroot):
        if sieve[i] != 0:
            m = int(n/i - i)
            sieve[i*i: n+1:i] = [0] * (m+1)
    sieve = [x for x in sieve if x !=0]
    return sieve

from math import *; from itertools import count, islice

def isPrime(n): #test if number is prime
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def zeventien(vanaf,bereik):
    import csv
    file = open('zeventien.txt','w')
    list=[]
    dicti = {
     1 : "one",
     2 : "two",
     3 : "three",
     4 : "four",
     5 : "five",
     6 : "six",
     7 : "zeven",
     8 : "eight",
     9 : "nine",
     10 : "ten",
     11 : "eleven",
     12 : "twelve",
     13 : "thirteen",
     14 : "fourteen",
     15 : "fifteen",
     16 : "sixteen",
     17 : "seventeen",
     18 : "eighteen",
     19 : "nineteen",
     20 : "twenty",
     30 : "thirty",
     40 : "fourty",
     50 : "fifty",
     60 : "sixty",
     70 : "seventy",
     80 : "eighty",
     90 : "ninety",
     100: "onehundred",
     200: "twohundred",
     300: "threehundred",
     400: "fourhundred",
     500: "fivehundred",
     600: "sixhundred",
     700: "sevenhundred",
     800: "eighthundred",
     900: "ninehundred",
     1000: "onethousand"
     }
    for i in range(vanaf,bereik+1):
        if i in dicti:
            list.append(dicti[i])
        elif i < 100:
            j = i % 10
            k = i - j
            list.append(dicti[k]+dicti[j])
        else :
            new_i = i % 100
            hontal = floor(i / 100)
            if new_i in dicti:
                list.append(dicti[hontal]+"hundredand"+dicti[new_i])
            else :
                e = i % 10
                tiental = (i%100)-e
                list.append(dicti[hontal]+"hundredand"+dicti[tiental]+dicti[e])
    slist = str(list)
    file.write(slist)
    #print(list)
    getallenrij = []
    for plak in range(vanaf-1,bereik):
        getallenrij += list[plak]
    return getallenrij
#print(zeventien(1,1000))

def deeltester(getal):
    delers=[]
    for n in range(1,getal):
        if (getal/n)%1 == 0:
            delers.append(n)
    return sum(delers)
#print(deeltester(220))

def eenentwintig(bereik):
    dict={}
    amic={}
    for n in range(1,bereik):
        dict[n]= deeltester(n)
        if n != dict.get(n):
            if n == dict.get(dict.get(n)):
                amic[n] = dict[n]
    return amic
#print(eenentwintig(10000))    

def twaalf(bereik,doel):
    #bereik is aantal trian nummers
    #doel is aantal delers van dat trian nummer
    prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    lijst=[]
    plist=[]
    som = []
    for n in range(1,bereik+1): 
        som.append(n)
        trian = sum(som)
        
        if len(lijst) == doel:
            #print(trian)
            break
        for p in prime:
            
            if (trian/p)%1 == 0:
                plist.append(p)
                if trian <= p:
                   
                   print(trian)
                   print(plist)
                   plist=[]
        """for d in range(1,trian+1):
            if (trian/d)%1 == 0:
                lijst.append(d)
                if trian == d:
                    print(trian)
                    print(lijst)
                    print(len(lijst))
                    print(plist)
                    if len(lijst) == doel:
                        print(trian)
                        break
                    lijst=[]"""
                         
from decimal import Decimal
def zesentwintig(bereik): #decimal repeating sequence length
    getcontext().prec = 4000
    for i in range(3,bereik+1):
        strFrac = str(Decimal(1)/Decimal(i)) #create decimal representation of the unit fractions
        if len(strFrac) > 27:
            for j in range(2,6):
                for k in range(-1,-500,-1):
                    decimals = strFrac[j:k] #grab decimals
                    repeater = principal_period(decimals) #Find repetition
                    if repeater:
#                         print("1/" + str(i) + " - " + strFrac + " (" +repeater+")" + "   " + str(len(repeater)))
                        if len(repeater) > 400:
                            print("1/" + str(i) + " - " + str(len(repeater)))
                        break
                if repeater:
                    break

def zevenentwintig(a,b,n):
    highest = 0
    f = open("test6.txt","a") #opens file with name of "test.txt"
    for i in range(-1000,a):
        for j in range(-1000,b):
            for teller in range(1,n):
#                 print(i)
                formResult =  (teller*teller) + (teller*i) + j
#                 if isPrime(formResult):
#                 f.write(str(teller) + "^2 + " + str(i) + "*" + str(teller) + " + " + str(j) + " = " + str(formResult)+ "  prime :D \n")
                if formResult < 1:
                    break
                if not isPrime(formResult):
                    if teller > highest:
                        highest = teller
                        f.write(str(teller) + "^2 + " + str(i) + "*" + str(teller) + " + " + str(j) + " = " + str(formResult)+ " no sigar \n")
                        highestFormula = (str(teller) + "^2 + " + str(i) + "*" + str(teller) + " + " + str(j) + " = " + str(formResult) + " wordt: " + str(-i*j))
                    break
    f.close()
    return highestFormula
#print(zevenentwintig(1000,1000,2000))
                
def Euler31(target): #count how many ways there are to make 2 pounds
    counter = 0 
    f = open("coin2.txt","a")
    for p100 in [0,1,2]:
         for p50 in [0,1,2,3,4]:
             for p20 in range(0,11):
                 for p10 in range(0,(21-2*p20)):
                     for p5 in range(0,(41-2*p10-10*p50)):
                         for p2 in range(0,101-5*p10-10*p20):
                            for p1 in range(0,(201-2*p2-10*p10-20*p20)):
                                if 100*p100+50*p50+20*p20+10*p10+5*p5+2*p2+p1==target:
                                    counter += 1
                                    f.write("€" + str(p100) + " + 50p=" + str(p50) + " + 20p=" + str(p20) + " + 10p=" + str(p10) + " + 5p=" +  str(p5) + " + 2p=" + str(p2) + " + 1p=" + str(p1) + " = 200  #" + str(counter) + "\n")
    f.close()
    return counter
# print(Euler31(20))

from fractions import Fraction
def Euler32(): #confusing fraction finder
    som = 1
    for noemer in range(10,100):
        for teller in range(10,noemer):
            a=int(str(teller)[0])
            b=int(str(teller)[1])
            c=int(str(noemer)[0])
            d=int(str(noemer)[1])
            if d != 0:
                if Fraction(teller,noemer) == Fraction(a,d) and b==c: #or Fraction(int(str(teller)[1]), int(str(noemer)[0])) or Fraction(int(str(teller)[0]), int(str(noemer)[1])) or Fraction(int(str(teller)[1]), int(str(noemer)[1]):
                    print(str(a) + "/" + str(d))
                    print(str(teller) + "/" + str(noemer) + "\n")
                    som *= Fraction(teller,noemer) 
    return som 
#print(Euler32())

