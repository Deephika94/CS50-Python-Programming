from random import randint

def get_level():
    while True:
        level = input("Level: ")
        try:
            if 0 < int(level) <=3:
                break
            else:
                continue
        except ValueError:
            continue
    return level

def generate_integer(level):
    if level == 1:
        x = randint(0,9)
        y = randint(0,9)
        return x,y
    elif level == 2:
        x = randint(10,99)
        y = randint(10,99)
        return x,y
    else:
        x = randint(100,999)
        y = randint(100,999)
        return x,y

def main():
    level = int(get_level())
    i = 1
    score = 0
    while i<=10:
        x,y = generate_integer(level)
        error = 1
        while True:
            print(f"{x} + {y} = ",end="")
            answer = int(input(""))
            if answer == x+y:
                score += 1
                break
            elif answer != x+y and error<3:
                print("EEE")
                error = error + 1
            else:
                print(f"{x} + {y} = {x+y}")
                break
        i += 1
    print("Score: ",score)

if __name__ == "__main__":
    main()
