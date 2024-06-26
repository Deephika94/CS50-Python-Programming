def main():
    ip_string = input("camelCase:")
    op_string = to_snakecase(ip_string)
    print(op_string)

def to_snakecase(string):
   op_str = ''
   for index in range(len(string)):
        if string[index].isupper() == False:
           op_str = op_str + string[index]
        else:
           op_str = op_str + "_" + string[index].lower()
   return str(op_str)

main()
