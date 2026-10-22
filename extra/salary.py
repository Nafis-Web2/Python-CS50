
def main():

    hours_worked = float(input("How many hour's have you worked? "))

    hourly_rate = float(input("what's the hourly pay rate? "))

    tax_percent = float(input("What is the tax %? "))

    gross_income = calculate_gross(hours_worked,hourly_rate)

    net_income = calculate_net(gross_income,tax_percent)

    print(f'Gross income = ${gross_income:.2f}')
    print(f'Net income = ${net_income:.2f}')







def calculate_gross(hours, rate):

    gross_income = hours * rate 

    return gross_income



def calculate_net(gross, tax):

    net_income = gross - (gross * tax / 100)

    return net_income


main()
