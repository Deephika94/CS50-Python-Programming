import tabulate
import sys
import csv

if len(sys.argv)<2:
    sys.exit("Too few command line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command line arguments")
elif sys.argv[1][-3:] != "csv":
    sys.exit("Not a CSV file")
else:
    try:
        table = []
        with open(sys.argv[1],"r") as file:
            line = csv.DictReader(file)
            for row in line:
                table.append(row)
        print(tabulate.tabulate(table,tablefmt="grid",headers="keys"))

       # table2=[]
       # with open(sys.argv[1],"r") as file:
       #     for line in file:
       #         row = line.rstrip().split(",")
       #         table2.append(row)
       # print(tabulate.tabulate(table2,tablefmt="grid",headers="firstrow"))

    except FileNotFoundError:
        sys.exit("File not found")
