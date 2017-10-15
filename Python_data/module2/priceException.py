while True:
    try:
        count = int(input("Enter count:"))
        price = int(input("Enter price for each one:"))
        print("Pay " + str(count * price))
        break
    except:
        print("Error,please enter numeric one.")
