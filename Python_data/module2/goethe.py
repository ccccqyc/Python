from math import sqrt


def isPrime(x):
    """is prime"""
    b = True;
    if x == 1:
        b = False;

    k = int(sqrt(x))
    for j in range(2, k + 1):
        if x % j == 0:
            b = False

    return b


# the primes list from 1 to 2000
list = [1, ]
for i in range(2, 2001):
    if isPrime(i):
        list.append(i)

for j in range(4, 2001, 2):
    for a in list:
        for b in list:
            if j == a + b:
                print(j, "=", a, "+", b)
