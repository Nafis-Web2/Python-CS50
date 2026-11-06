

def main():

    camel_case = input("Enter a name in camelCase: ")

    converted_name = convert(camel_case)

    print(converted_name)


def convert(name):
    # Initialize the variable with an empty string
    converted = ""

    # Loop through each character in name
    for chars in name:

        # Check if the current character is uppercase
        if chars.isupper():

            # Add an underscore and the lowercase character
            converted += "_" + chars.lower()

        else:
            # Add the character unchanged
            converted += chars

    # Return the completed snake_case string
    return converted

main()