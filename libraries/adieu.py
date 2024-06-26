import inflect
names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print ("Adieu, adieu, to ",end ="")
        for i in range(len(names)):
            if i+1 < len(names) and len(names)>2:
                print(names[i],end=", ")
            elif i+1 >= len(names) and len(names)>2:
                print("and",names[i])
            elif len(names)==1:
                print(names[i])
            else:
                print(names[i],"and",names[i+1])
                break
        break
