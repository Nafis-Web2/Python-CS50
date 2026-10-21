
def main():
    celsius = float(input("Enter a tempreture in celsius. "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"Temperature to Fahrenheit = {fahrenheit:.2f}")





def celsius_to_fahrenheit(c):
    function = (c * 1.8) + 32
    return function



main()
