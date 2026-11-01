

def main():

    employee_name = input("Enter employee name: ")
    annual_salary = float(input("Enter annual salary: "))
    years_of_service = float(input("Enter years of service: "))
    performance_rating = int(input("Enter rating 1/2/3/4/5: "))

    validation = input_validation(annual_salary,years_of_service,performance_rating)
    
    if validation == True:
            perform_bon = performance_bonus(annual_salary,performance_rating,years_of_service)
            loyalty_bon = loyalty_bonus(annual_salary,years_of_service,performance_rating)

            total_bonus = perform_bon + loyalty_bon

            final_compensation = final_comp(annual_salary,total_bonus)

            print(f'Employee name: {employee_name}\nAnnual salary: {annual_salary:.2f}\nPerformance bonus: {perform_bon:.2f}\nLoyalty bonus: {loyalty_bon:.2f}\nTotal bonus: {total_bonus:.2f}\nFinal compensation: {final_compensation:.2f}')
    else:
          print(validation)

def input_validation(salary,serivce_years,performance):

    if salary < 0:
        return "Salary cannot be negative."
    elif serivce_years < 0 :
            return "Service years cannot be negative."
    elif performance < 1:
        return "Enter a valid rating from 1-5"
    elif performance > 5:
         return "Enter a valid rating from 1-5"
    else:
         return True

def performance_bonus(annual_salary,performance_rating,years_of_service):

    if years_of_service < 2: 
        if performance_rating == 4 or performance_rating == 5:
          return annual_salary * (5/100)
    
    if performance_rating == 5:
          return annual_salary * (15/100)
    elif performance_rating == 4:
              return annual_salary * (10/100)
    elif performance_rating == 3:
              return annual_salary * (5/100)
    elif performance_rating == 2:
              return annual_salary * (2/100)
    elif performance_rating == 1:
              return annual_salary * (0/100)

def loyalty_bonus(annual_salary,years_of_service,performance_rating):

      if years_of_service >= 5 and performance_rating > 1:
            return annual_salary * 3 / 100
      
      if years_of_service < 5:
            return annual_salary * 0 / 100

      if performance_rating == 1:
            return annual_salary * 0 / 100

def final_comp(annual_salary,total_bonus):

      final_compensation = annual_salary + total_bonus

      return final_compensation


main()