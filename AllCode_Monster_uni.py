
from Teacher_class import *
from Student_class import *
from Monster_class import *
from workshop_class import  *

# (user input 1)
# As a Receptionist of the University, I should be able to create a Student with only first and last name

# Create empty list called students & teachers
list_of_students = []
list_of_teacher = []
# create empty list for workshop
list_of_workshop = []
list_of_attendees = []
list_all_workshops = []
# create a student_id_counter
student_id = 0
# create a teacher_id_counter
teacher_id = 0
#
f_name_student = ' '
l_name_student = ' '
workshop_subject = ' '

user_input = ' '
# # With every iteration of the while loop:
while (user_input != '5'):
        user_input = input("Please press enter the number linked to the option you would like.\n 1) Create a student. \n 2) Create a teacher. \n 3) Create workshop \n 4) View list. \n 5) Quit programme. \n")

        if user_input == '1':
            # increment the student_id_counter
            student_id = student_id + 1

            # ask for user input (names)
            f_name_student = input("Enter first name of student \n")
            l_name_student = input("Enter last name of student \n")

            # create a student from those inputs
            student = Student(f_name_student, l_name_student, student_id)

            # add that student to the list of students
            list_of_students.append(student)
            print(f"Student name: {f_name_student} {l_name_student} {student_id}")

            # print(list_of_students)
            print("Number of students in list: " + str(len(list_of_students)))

# As a Receptionist of the University, I should be able to create a Teacher
# With every iteration of the while loop:
        # make condition for teacher
        if user_input == '2':

            # increment the teacher_id_counter
            teacher_id = teacher_id + 1

            # ask for user input (names)
            f_name_teacher = input("Enter first name of teacher \n")
            l_name_teacher = input("Enter last name teacher \n")

            # create a teacher from those inputs
            teacher = Teacher(f_name_teacher, l_name_teacher, teacher_id)

            # add that student to the list of students
            list_of_teacher.append(teacher)
            print(f"Teacher name: {f_name_teacher} {l_name_teacher} {teacher_id}")

            # print(list_of_students)
            print("Number of teacher in list: " + str(len(list_of_teacher)))


        if user_input == '3':

            workshop_subject = input('What subject will the class be ?')
            workshop_teacher = input("what teacher will be taking the class ?")
            workshop_list_of_attendees = input("Enter list of Attendees: ")
            print("Subject: ", workshop_subject)
            print("Teacher:", workshop_teacher)
            print("Attendess:", workshop_list_of_attendees)

        if user_input == '4':
            list_all_workshops = (workshop_subject + ', ' + workshop_teacher)
            print(list_all_workshops)

        if user_input == '5':
            print("Programme ended")
            break
