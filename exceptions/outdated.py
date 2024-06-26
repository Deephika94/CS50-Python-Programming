month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
month_no = list(range(1,13))
month_dict = dict(zip(month,month_no))

while True:
    try:
        date = input("Date:").strip()
        if(date.find("/")) != -1:
            m,d,y = date.split("/")
            if len(m) <= 2 and int(m) <=12 and len(d) <=2 and int(d)<=31 and len(y) ==4:
                print(f"{y}-{int(m):02}-{int(d):02}",sep="")
                break
            else:
                continue
        else:
            m,d,y = date.split(" ")
            d,comma = d.split(",")
            if m in month and len(d)<=2 and int(d)<=31 and len(y) ==4:
                print(f"{y}-{int(month_dict[m]):02}-{int(d):02}")
                break
            else:
                continue
    except ValueError:
        continue


