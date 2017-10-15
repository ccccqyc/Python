from random import randint

x = randint(0, 300)
print(x)
digit = int(input("please input a num between 0~300 \n>"))
if digit == x:
    print("bingo")
elif digit > x:
    print("too large")
else:
    print("too samll")

x = str(x);
for s in x:
    print(s)
