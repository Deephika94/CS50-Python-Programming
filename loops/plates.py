def main():
    plate = input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    length_test = check_length(s)
    start_test = check_start(s)
    splchar_test = check_splchar(s)
    endnum_test = check_endnum(s)
    zero_test = check_zero(s)
    return length_test and start_test and splchar_test and endnum_test and zero_test

def check_zero(s):
    for i in range(len(s)):
        if s[i].isnumeric() == True:
            if s[i] == "0":
                return False
            else:
                return True
        else:
            continue
    return True

def check_endnum(s):
    if s.isalpha() == True:
        return True
    else:
        for i in range(len(s)):
            if s[i].isnumeric()==True:
                if s[i:len(s)].isnumeric() == True:
                    return True
                else:
                    return False
            else:
                continue

def check_length(s):
    if  2 <= len(s) <=6:
        return True
    else:
        return False

def check_start(s):
    return s[0:2].isalpha()

def check_splchar(s):
    return s.isalnum()

main()
