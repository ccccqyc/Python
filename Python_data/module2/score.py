score = int(input("Please enter your score :"))
if 90 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 0 <= score <= 59:
    print("B")
else:
    print("invalid score")