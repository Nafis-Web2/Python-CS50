
def main():

    name = input("Student Name: ")

    num_of_courses = int(input("How many courses are you taking: "))


    while num_of_courses < 3 or num_of_courses > 6:
        num_of_courses = int(input("Enter between 3-6 courses: "))

    courses = []

    for n in range(num_of_courses):

        Course_name = input("Enter course name: ")

        mid_term_score = float(input("Enter your mid-term score: "))

        while mid_term_score < 0 or mid_term_score > 100:
             mid_term_score = float(input("Enter your mid-term score between 0-100: "))

        final_exam_score = float(input("Enter your final exam score: "))

        while final_exam_score < 0 or final_exam_score > 100:
            final_exam_score = float(input("Enter your final exam score between 0-100: "))

        homework_score = float(input("Enter your final homework score: "))

        while homework_score < 0 or homework_score > 100:
            homework_score = float(input("Enter your final homework score between 0-100: "))
        
        course_info = {
        "course_name": Course_name,
        "mid_term_score" : mid_term_score,
        "final_exam_score" : final_exam_score,
        "homework_score" : homework_score
        }

        courses.append(course_info)

main()