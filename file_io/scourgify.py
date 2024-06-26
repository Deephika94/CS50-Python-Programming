import csv
import sys

if len(sys.argv)<3:
    sys.exit("Too few command line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command line arguments")
elif sys.argv[1][-3:] != "csv":
    sys.exit("Not a CSV file")
elif sys.argv[2][-3:] != "csv":
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            students = csv.DictReader(file)
            student_list = []
            for student in students:
                last,first = student['name'].split(",")
                house = student['house']
                student_list.append({"first":first.lstrip(),"last":last,"house":house})
        to_file = open(sys.argv[2],"w")
        writer = csv.DictWriter(to_file,fieldnames=["first","last","house"])
        writer.writeheader()
        writer.writerows(student_list)
        to_file.close()
    except FileNotFoundError:
        sys.exit("File not found")
