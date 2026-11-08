
def main():

    password = input("Enter Password: ")

    pass_digits = 0

    for digits in password:
        if digits.isdigit():
            pass_digits += 1

    if len(password) >= 8 and pass_digits >= 2:
        print("Strong Password")
    else:
        print("Weak Password")

main()
