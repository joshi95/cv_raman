# We will make a program which will get the average marks of student.
# input will be an n which will denote no of students
# after that you will take input m which will tell the no of subjects
# after this you will take n students names and take their subject marks



# "no of students ?": 5
# "no of subjects ?": 2
# "give the inputs: "
# "sadaf"
# "give the marks in subjects":
# 10 20
# "Asif"
# "give the marks in subjects":
# 10 20
# "output":
# Sadaf: 103
# Asif: 102

# whenever you want to take space seperated values as input

def get_total_students_and_subjects():
    print("Please enter the no of students: ", end="")
    no_of_students = int(input())
    print("Please enter the no of subjects: ", end="")
    no_of_subjects = int(input())
    return (no_of_students, no_of_subjects)

def get_average(scores):
    sum_of_all_marks = 0
    for score in scores:
        sum_of_all_marks += score
    return sum_of_all_marks // len(scores)


def main():
    no_of_students, no_of_subjects = get_total_students_and_subjects()

    score_dict = {}
    for i in range(no_of_students):
        print("Please enter student name: ", end="")
        student_name = input()
        print("Please enter the marks of", student_name)
        scores = list(map(int, input().split(" ")))[:no_of_subjects] 
        score_dict[student_name] = get_average(scores)


main()
