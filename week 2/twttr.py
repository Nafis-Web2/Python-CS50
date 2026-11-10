
def main():

    text = input("Enter a text: ")

    new_text = ""

    for chars in text:
        if chars == "a" or chars == "A":
            continue
        elif chars == "e" or chars == "E":
            continue
        elif chars == "i" or chars == "I":
            continue
        elif chars == "o" or chars == "O":
            continue
        elif chars == "u" or chars == "U":
            continue    
        new_text += chars
    print(new_text)

main()
