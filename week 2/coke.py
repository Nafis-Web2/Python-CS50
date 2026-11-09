
def main():
    # start with a given value of 50
    start = 50
    #while start is greater then 0 
    while start > 0:
        #print the amount owed
        print(f'Amount Due: {start}')
        # ask for the coins to insert
        coins = int(input("Insert coins: "))
        #check weather the coins are 5,10,25 and if they
        # are subtract that coin from the starting value
        # keep looping until we reach 0
        if coins == 5:
            start -= 5
        elif coins == 10:
            start -= 10
        elif coins == 25:
            start -= 25


    # this will return how much the machine owes us if we overpay
    print(f'Change Owed: {-start}') # the negative infront makes the negaitve owed in to a positive number

main()
                
        
    