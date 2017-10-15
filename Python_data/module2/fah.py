def fah(F):
    C = 5 / 9 * (F - 32)
    return str(C)


for i in range(0, 301, 20):
    print(str(i) + " : " + fah(i))
