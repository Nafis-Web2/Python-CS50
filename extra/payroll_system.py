

def main():

    employee_name = input("Employee Name: ")
    hours_worked = float(input("Hours Worked: "))
    hourly_pay_rate = float(input("Hourly Pay Rate: "))
    performance_rating = input("Performance Rating: excellent, good, average, poor ")
    years_of_service = float(input("Years of Service: "))
    tax_percentage = float(input("Tax percentage: "))

    valid = input_validation(employee_name,hours_worked,hourly_pay_rate,performance_rating,years_of_service,tax_percentage)



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