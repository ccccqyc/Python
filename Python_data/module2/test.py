from math import sqrt


# 缓存默尼森数 
cacheMonisen = []

# 缓存素数 
cachePrime = []

# 素数范围，搜索更多的素数 
minNumber = 2
maxNumber = 100

def isPrime(x):
    '''判断是不是素数'''
    k = int(sqrt(x))
    for i in range(2, k + 1):
        if x % i == 0:
            return False
    return True
def addCachePrime():
    '''增加素数缓存'''
    for i in range(minNumber, maxNumber):
        if isPrime(i) and (i not in cachePrime):
            cachePrime.append(i)
def monisen(no):
    '''求解第N个默尼森数'''

    # 初始化素数缓存 
    addCachePrime()

    if no <= len(cacheMonisen):
        return cacheMonisen[no - 1]

    for i in cachePrime:
        # M和P均为素数 
        p = i
        m = pow(2, p) - 1
        if isPrime(p) and isPrime(m):
            cacheMonisen.append(m)
        if no == len(cacheMonisen):
            break

    if no == len(cacheMonisen):
        return cacheMonisen[-1]

    else:
        # 素数范围不足，须增加素数，继续查找 
        global minNumber, maxNumber
        minNumber, maxNumber = maxNumber, maxNumber * 2
        return monisen(no)
print(monisen(int(input())))