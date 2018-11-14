def fibbonaci(limit):
    a = 0
    b = 1
    c = 0
    som = 0
    while b < limit:
        c = a + b
        a = b
        b = c
        if 0 == b % 2:
            som += b
    return som

def traagdrie(limit):
    teller = round(limit/2)
    while teller > 1:
        if (limit/teller) % 1 == 0:
            return teller
        else:
            teller += -1

def sneldrie(getal, limit):
    teller = 2
    factor = []
    while teller <= limit:
        if (getal/teller) % 1 == 0:
            factor.append(teller)
            getal = getal/teller
            teller = 2
        else:
            teller += 1
    return factor
#print(max(sneldrie(600851475143,10000)))

def traagvijf(limit,maxdeler):
    teller = 2
    deler = 2
    while teller <= limit:
        while deler <= maxdeler:
                if deler == maxdeler:
                    return teller
                elif teller == limit:
                    return "Bereik te klein"
                elif (teller/deler) % 1 != 0:
                    teller += 1
                    deler = 2
                elif (teller/deler) % 1 == 0:
                    deler += 1

def zes(limit):
    teller = 1
    steller = 1
    som = 0
    squaresom = 0
    while teller<=limit:
        som += teller
        teller += 1
    som = som**2
    while steller<=limit:
        squaresom += steller**2
        steller += 1
    verschil =  som - squaresom
    return verschil
#print(zes(100))

def prime(limit):
    teller = 3
    deler = 3
    result = [2] #Dit algoritme voelt zich te goed om op even getallen te checken
    while teller < limit-1:
        deler = 3
        while deler <= teller:
            if teller == deler:
                #Als de deler dezelfde waarde heeft bereikt als de teller dan,
                #is ie onderweg dus niet onderbroken door de elif-statement en dus een priem
                result.append(teller)
            elif (teller/deler) % 1 == 0:
                #Is ie deelbaar? NEXT!!
                teller += 2
                deler = 3
            deler += 2
        teller += 2
    return result
#print (sum(prime(2000)))

def acht():
    getal = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    result = []
    for i in range(len(getal)):
        if len(getal[i:i+5]) == 5:
            result.append(int(getal[i])*int(getal[i+1])*int(getal[i+2])*int(getal[i+3])*int(getal[i+4]))
    return result
#print(max(acht()))
def negen():
    for c in range(1,1000):
        for b in range(1,c):
            for a in range(1,b):
                if a**2+b**2 == c**2 and a+b+c == 1000:
                    return a*b*c
#print(negen())
def elf():

    L = []
    L.append("08 82 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
    L.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
    L.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
    L.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
    L.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
    L.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
    L.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
    L.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
    L.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
    L.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
    L.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
    L.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
    L.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
    L.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
    L.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
    L.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
    L.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
    L.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
    L.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
    L.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
    G = []
    for vert in range(0,20):
        for hors in range(0,49,3):
            G.append(int(L[vert][hors:hors+2])*int(L[vert][hors+3:hors+5])*int(L[vert][hors+6:hors+8])*int(L[vert][hors+9:hors+11]))
    for hors in range(0,60,3):
        for vert in range(0,17):
            G.append((int(L[vert][hors:hors+2])*int(L[vert+1][hors:hors+2])*int(L[vert+2][hors:hors+2])*int(L[vert+3][hors:hors+2])))
    for vert in range(0,17):
        for hors in range(0,49,3):
            G.append(int(L[vert][hors:hors+2])*int(L[vert+1][hors+3:hors+5])*int(L[vert+2][hors+6:hors+8])*int(L[vert+3][hors+9:hors+11]))
    for vert in range(0,17):
        for hors in range(9,60,3):
            G.append((int(L[vert][hors:hors+2])*int(L[vert+1][hors-3:hors-1])*int(L[vert+2][hors-6:hors-4])*int(L[vert+3][hors-9:hors-7])))
    return max(G)
#print(elf())
#def twaalf():
def zestien(macht):
    nummer = str(2**macht)
    som = 0
    for i in range(0,len(nummer)):
        som += int(nummer[i])
    return som
#print(zestien(1000))

def twintig(fact):
    import math
    nummer = str(math.factorial(fact))
    som = 0
    for i in range(0,len(nummer)):
        som += int(nummer[i])
    return som
#print(twintig(100))

def primes(n): 
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
print(primes(127))

def veertientraag(bereik):
    stappen = []
    for n in range(1,bereik):
        list.append(n)
        while n > 1:
            if n%2 == 0:
                n = int(n/2)
                list.append(n)
            elif n%2 != 0:
                n = int((3*n) + 1)
                list.append(n)
        stappen.append(len(list))
    m = max(stappen)
    p = stappen.index(m)+1
    return p, m
"""def achtien():
    L=[]
    L.append("3")
    L.append("7 4")
    L.append("2 4 6")
    #L.append("8 5 9 3")
    num_lines = sum(1 for line in L)
    while vert in range(0,num_lines+1):
        print(vert,hors)            
        L.append(int(L[vert][hors:hors+2])
    return num_lines
#print(achtien())"""
















