total = int(50)
while total > 0:
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        total = total - coin
        if total > 0:
            print("Amount Due:", total)
        else:
            print("Change Owed:", abs(total))
    else:
        print("Amount Due:", total)
        continue