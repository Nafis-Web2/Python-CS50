

def main():

    employee_name = input("Employee Name: ")
    hours_worked = float(input("Hours Worked: "))
    hourly_pay_rate = float(input("Hourly Pay Rate: "))
    performance_rating = input("Performance Rating: excellent, good, average, poor: ")
    years_of_service = float(input("Years of Service: "))
    tax_percentage = float(input("Tax percentage: "))

    valid = input_validation(employee_name,hours_worked,hourly_pay_rate,performance_rating,years_of_service,tax_percentage)

    if valid != True:
        print(valid)
        return

    gross_income = calculate_gross_income(hours_worked,hourly_pay_rate)

    bonus_income = performance_bonus(performance_rating,gross_income)

    loyal_bonus = loyalty_bonus(years_of_service,gross_income)

    total = gross_income + bonus_income + loyal_bonus

    total_tax = total * tax_percentage / 100
    
    net_income = total - total_tax

    print("\n========== EMPLOYEE PAYROLL SUMMARY ==========")
    print(f"Employee Name: {employee_name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Pay Rate: ${hourly_pay_rate:.2f}")
    print(f"Gross Income: ${gross_income:.2f}")
    print(f"Performance Bonus: ${bonus_income:.2f}")
    print(f"Loyalty Bonus: ${loyal_bonus:.2f}")
    print(f"Total Income Before Taxes: ${total:.2f}")
    print(f"Tax Deducted: ${total_tax:.2f}")
    print(f"Net Income: ${net_income:.2f}")
    print("==============================================")


def input_validation(name,hours,rate,performance,service_years,tax):

    if not name.strip():
        return "Invalid name"
    if hours < 0 or hours > 80:
        return "Hours worked must be between 0 and 80."
    if rate <= 0:
        return "Hourly pay rate must be greater than 0."

    performance = performance.strip().lower()

    if performance != "excellent" and performance != "good" and performance != "average" and performance != "poor":
        return "Invalid performance rating. Choose excellent, good, average, or poor."
    
    if not service_years.is_integer() or service_years < 0:
        return "Invalid years of service. Must be a non-negative whole number."
    if tax < 0 or tax > 40:
        return "Invalid tax percentage. Must be between 0 and 40."
    else:
        return True


def calculate_gross_income(hours,rate):

    if hours <= 40:
        return hours * rate
    if hours > 40:
        return 40 * rate + (hours - 40 )  * rate * 1.5

def performance_bonus(performance,gross):

    performance = performance.lower().strip()

    if performance == "excellent":
        return gross * 0.15
    if performance == "good":
        return gross * 0.10
    if performance == "average":
        return gross * 0.05
    if performance == "poor":
        return gross * 0

def loyalty_bonus(years,gross):

    if years >= 0 and years <= 2:
        return gross * 0
    if years >= 3 and years <=5:
        return gross * 0.03
    if years >=6 and years <= 10:
        return gross * 0.05
    if years > 10:
        return gross * 0.08

main()