import random

while True:
    level = input("Level: ")
    try:
        if int(level) >=0:
            break
        else:
            continue
    except ValueError:
        continue

number = random.randint(1,int(level))

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break

