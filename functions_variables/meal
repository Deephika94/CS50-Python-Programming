def main():
    t = input("what time is it:? ")
    meal = convert(t)
    if 7.0 <= meal <=8.0:
        print("breakfast time")
    elif 12.0 <= meal <= 13.0:
        print("lunch time")
    elif 18.0 <= meal <= 19.0:
        print("dinner time")

def convert(tm):
    hr,m = tm.split(":")
    min = float(m) / 60
    dur = float(hr) + min
    return float(dur)

if __name__ == "__main__":
    main()
