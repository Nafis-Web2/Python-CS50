

def main():

    grade = input("What is you'r grade: ")

    score = float(grade)

    if score > 100 or score < 0:
        print("Invalid grade.Please enter a valid grade.")

    elif score >= 90:
        print("A")

    elif score >= 80:

        print("B")

    elif score >= 70:
        print("C")

    elif score >= 60:
        print("D")

    else:
        print("F")




main()




                  