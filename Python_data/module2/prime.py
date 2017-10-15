from math import sqrt

def isPrime(x):
    'is prime'
    b = True;
    if x==1:
        b = False;

    k = int(sqrt(x))
    for j in range(2,k+1):
        if x%j == 0:
            b = False

    return b

for i in range(2,101):
    if isPrime(i):
        print(i,end=' ')