from Monster_class import *
from workshop_class import *
from Student_class import *
from Teacher_class import *

# As a Receptionist of the University, I should be able to create a Student with only first and last name

student1 = Student('Fred', 'Alfredo', 1)
student2 = Student('Max', 'Skywalker', 2)
student3 = Student('Mahan', 'Jahromi', 3)

# Attempt 1)
#
# while True:
#     f_name = input('Enter first name \n')
#     l_name = input('Enter last name \n')
#     student = Student(f_name, l_name, 4)
#     print(student.f_name, student.l_name)


# Create empty list called students
# list_of_students = []
#
# student
# have a student_id_counter
# witch every iteration of the while






# print(student1)
# print(student1.f_name, student1.l_name)
# print(student2)
# print(student2.f_name, student2.l_name)
# # print(student3)
# # print(student3.f_name, student3.l_name)
#
# list_attendees_create = []
#
# list_attendees_create.append(student1)
# list_attendees_create.append(student2)
# list_attendees_create.append(student3)
#
# for Student in list_attendees_create:
#     print(Student.f_name, Student.l_name)

# do same for teacher
#

# workshop1 = Workshop('math', 'Mr Jo')
# workshop2 = Workshop('Chem', 'Mr Mahan')
#
# list_of_workshop = []
#
# list_of_workshop.append(workshop1.make_workshop())
# list_of_workshop.append(workshop2.make_workshop())
#
# print(list_of_workshop)
#
# workshop_subject = input('What subject would are you looking for? \n')
# workshop_teacher = input('You are the teacher what is your name? \n')
#
# workshop_test = f'The workshop subject is {workshop_subject} and the teacher is {workshop_teacher}'
# print(workshop_test)

student1.skills.append('scary_face')
student1.skills.append('fire_ball_jutsu')
student1.skills.append('stealth')
print(student1.skills)


