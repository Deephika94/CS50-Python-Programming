def amount(greet):
    if greet.startswith("hello") == True:
        print("$0")
    elif greet.startswith("h")== True:
        print("$20")
    else:
        print("$100")

def main():
    g = input("Say your greetings:").strip().lower()
    amount(g)


main()