def main():
    message = input(str("Enter a message here. "))

    print(convert(message))

def convert(message):
    message = message.replace(":)" , "🙂")
    
    message = message.replace(":(" , "🙁")

    return message

main()

