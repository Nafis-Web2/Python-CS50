
def main():

    plate = input("Enter the plate number you want: ")

    is_plate_valid = is_valid(plate)

    if is_plate_valid == True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate_n):
    if len(plate_n) >= 2 and len(plate_n) <= 6:
        if plate_n[0].isalpha() and plate_n[1].isalpha():
            pass
        else:
            return False
    else:
        return False

    number_found = False

    for i in plate_n:
        if i.isdigit():
            if i == "0" and number_found == False:
                return False
            number_found = True
        elif number_found == True and i.isalpha():
            return False

    if plate_n.isalnum():
        pass
    else:
        return False

    return True


main()