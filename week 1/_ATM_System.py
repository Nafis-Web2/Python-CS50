
def main():

    balance = 1000

    how_much_to_withdraw = input("How much money would you like to withdraw today? ")

    withdrawal = float(how_much_to_withdraw)

    if withdrawal > balance:
        print("Insufficient funds.")
    elif withdrawal <= 0:
        print("Invalid withdrawal amount.")
    elif withdrawal % 20 != 0:
        print("ATM only accepts multiples of $20.")
    else:
        balance = balance - withdrawal
        print(balance)
    
    



main()



