
def main():

    customer_name = input("Customer Name: ")
    elec_usage = float(input("Enter electricity usage in kWh: "))
    customer_type = input("Residential or Business: ")

    valid = validation(elec_usage,customer_type)



    if valid == True:
        charge = calculate_charge(elec_usage)
        discount_off = discount(customer_type,charge)

        bill = final_bill(charge,discount_off)

        print(f'Customer name: {customer_name}\nElectricity usage (kWh): {elec_usage:.2f}\nElectricity charge before discount: {charge:.2f}\nDiscount amount: {discount_off:.2f}\nService fee ($8.00)\nFinal bill: {bill:.2f}')

    else:
        print(valid)



def validation(kWh,type):

    if kWh < 0:
        return "Invalid kWh"
    elif type != "Residential" and type != "Business":
        return "Invalid type"
    else:
        return True

def calculate_charge(usage):

    if usage <= 100:
        return usage * 0.12
    elif  usage <= 300:
        return 100 * 0.12 + ((usage - 100) * 0.15)
    elif usage > 300:
        return 100 * 0.12 + 200 * 0.15 + ((usage - 300) * 0.20)

def discount(type,charge):

    if type == "Residential":
        return charge * 0.05
    elif type == "Business":
        return charge * 0

def final_bill(charge,discount):

    final = charge - discount + 8
    return final


    
main()