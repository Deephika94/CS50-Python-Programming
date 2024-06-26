
def to_check(name):
    match name:
        case "42" |"FORTY TWO" | "FORTY-TWO":
            print("Yes")
        case _:
            print("No")

deep_input = input("What is the answer to the great question of life, the universe and everything? ").strip().upper()

to_check(deep_input)
