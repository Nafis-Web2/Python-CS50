
def main():

    age = int(input("Enter your age: "))

    annual_income = float(input("Enter you annual income: "))

    credit_score = int(input("Enter your credit score: "))

    monthly_debt = float(input("Enter the monthly debt payments: "))

    dti = calculate_dti(annual_income,monthly_debt)


    print(f'Debt-to-Income Ratio:{dti:.2f}%')

    eligibility = check_eligibility(age,annual_income,credit_score,dti)

    print(eligibility)





def calculate_dti(annual_income, monthly_debt):

    monthly_income = annual_income / 12


    dti = (monthly_debt / monthly_income) * 100

    return dti


def check_eligibility(age,income,credit_score,dti):

    if age < 18:
        return "Loan Denied: Applicant must be at least 18 years old."

    elif income < 30000:
        return "Loan Denied: Annual income is too low."

    elif credit_score < 650:
        return "Loan Denied: Credit score is too low."

    elif dti > 35:
        return "Loan Denied: Debt-to-income ratio is too high."

    elif credit_score >= 750 and dti <= 35:
        return "Loan Approved: Excellent credit!"
    
    elif credit_score >= 700:
        return "Loan Approved: Good credit!"
    
    else:
        return "Loan Approved: Fair credit!"


main()