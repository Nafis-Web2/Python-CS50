
def main():

    exam_number = int(input("How many exam's have you taken: "))

    scores = 0

    for number in range(exam_number):
        exam_scores = int(input("Enter Exam score: "))
        scores += exam_scores

    avg_scores = scores / exam_number

    if avg_scores >= 70:
        print(f'Passed: {avg_scores:.2f}')
    else:
        print(f'Failed: {avg_scores:.2f}')
    


main()
