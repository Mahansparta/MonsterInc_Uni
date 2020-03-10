from Monster_class import *

class Student(Monster):

    def __init__(self, f_name, l_name, studentID):
        super().__init__(f_name, l_name)
        self.studentID = studentID
        self.student_skill = []

   # As a Receptionist of the University, I should be able add skills to a student object


    def add_skill(self):
        skill_to_add = input('What skill would you like to add?\n')



