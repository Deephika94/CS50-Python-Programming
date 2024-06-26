import sys

if len(sys.argv)>2:
    sys.exit("Too many arguments")
elif len(sys.argv)<2:
    sys.exit("Too few arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a python file")
else:
    try:
        with open(sys.argv[1],"r") as file:
            count = 0
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith("#") or line == "\n":
                    pass
                else:
                    count+= 1
        print(count)

    except (FileNotFoundError,ValueError):
        sys.exit("File does not exist")

    except IndexError:
        sys.exit("Too few arguments")
