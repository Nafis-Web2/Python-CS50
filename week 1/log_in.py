

def main():

    correct_username = "admin"

    correct_password = "python123"

    get_username = input('Enter username: ')

    get_password = input('Enter password: ')

    if get_username == correct_username:
        if get_password == correct_password:
            print("correct credentials")
        else:
            print("Password not valid!")
    else:
        print("Username not valid!")

main()