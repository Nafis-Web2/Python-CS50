

def main():

    num_1 = int(float(input("Enter your first number: ")))

    operation = input("enter operation: +,-,*, or /: ") 

    num_2 = int(float(input("Enter your second number: ")))



    calculate_num = calculate(num_1,num_2,operation)

    if isinstance(calculate_num, float):
        print(f'{calculate_num:.2f}')
    else:
        print(calculate_num) 


def calculate(n1,n2,op):

    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return n1/n2

    else:
        return "Invalid operation!"
    

    
main()
