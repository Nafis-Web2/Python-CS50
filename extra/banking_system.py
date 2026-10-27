
def main():

    customer_name = input("Enter name: ")
    account_balance = float(input("Enter balance: "))
    account_type = str(input("Enter account type: "))
    transaction_type = input("Enter transaction type: ")
    transaction_amount = float(input("Enter trans action amount: "))

    print(customer_name)

    if transaction_type == "deposit":
        result = deposit(account_balance,transaction_amount)

        if isinstance(result,float):
            print(f'{result:.2f}')
        else:
            print(result)

    elif transaction_type == "withdraw":
        result = withdraw(account_balance,transaction_amount,account_type)

        if isinstance(result,float):
            print(f'{result:.2f}')
        else:
            print(result)

    elif transaction_type == "balance":
        result = balance_inquiry(account_balance)

        if isinstance(result,float):
            print(f'{result:.2f}')
        else:
            print(result)

    else:
        print("Invalid transaction type.")

def deposit(balance, amount):

    if amount <= 0:
        return "Transaction Denied: Invalid deposit amount."
    else:
        return balance + amount


def withdraw(balance,amount,account_type):
    account_balance = amount

    if amount <= 0:
        return "Transaction Denied: Invalid withdrawal amount."
    elif account_type == "savings":
        account_balance += 2
    elif account_type == "checking":
        account_balance += 1

    

    if account_balance > balance:
        return "Transaction Denied: Insufficient funds."

    if account_type == "savings" and balance - account_balance < 100:
        return "Transaction Denied: Savings accounts must maintain $100."
    else:
        return balance - account_balance
    

def balance_inquiry(balance):
    return float(balance)


main()