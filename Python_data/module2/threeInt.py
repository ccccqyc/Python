def theOtherTwo(n):
    b = False
    listIndex = [n // 100, n // 10 % 10, n % 10]
    listTwo = listIndex[0] + listIndex[2] * 10 + listIndex[1] * 100
    listThree = listIndex[1] + listIndex[0] * 10 + listIndex[2] * 100
    if listTwo % 37 == listThree % 37 == 0:
        b = True
    return b


i = int(input("num:/n>"))

if i % 37 == 0:
    print(theOtherTwo(i))
else:
    print(False)
