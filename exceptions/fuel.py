while True:
    try:
        while True:
            fraction = input("Fraction: ")
            a,b = fraction.split("/")
            a = int(a)
            b = int(b)
            if a<=b:
                percentage = (int(a)/int(b))*100
                if percentage <= 1:
                    print("E")
                elif percentage >= 99:
                    print("F")
                else:
                    print(f"{percentage:.0f}%")
                break
            else:
                continue
        break
    except (ValueError,ZeroDivisionError):
        continue

