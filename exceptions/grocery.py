def main():
    grocery_dict = {}
    while True:
        try:
            item = input("")
            if item in grocery_dict:
                count = grocery_dict[item] + 1
                grocery_dict[item] = count
            else:
                grocery_dict |= {item:1}
        except EOFError:
            print()
            break
    sorted_grocery_dict = dict(sorted(grocery_dict.items()))
    for key in sorted_grocery_dict:
        print(sorted_grocery_dict[key],key.upper(),sep=" ")

main()
