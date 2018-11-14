from root.ProjectEuler549 import primeList, isPrime


def IntegerRotations(a):
    rotations = []
    twice = (str(a) + str(a))
    for b in range(0, len(str(a))):
        rotation = ''
        for c in range(0, len(str(a))):
            rotation += twice[b+c]
        rotations.append(int(rotation))
    return(rotations)

def rotationalPrimeList(x):
    test = primeList(x)
    var = []
    teller = 0
    for a in test:
        counter = 0
        countTill = len(str(a))
        for b in IntegerRotations(a):
            if isPrime(b) is False:
                break
            counter += 1
#             print("prime #" + str(counter) + " is " + str(b))
            if counter == countTill:
                print("got one " + str(b))
                var.append(a)
    print("# of rotational primes in set: " + str(len(var)))
    return var
print(rotationalPrimeList(1000000))

# print(isPrime(017))