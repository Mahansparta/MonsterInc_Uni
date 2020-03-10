from Monster_class import *

class Teacher(Monster):

    def __init__(self, f_name_teacher, l_name_teacher, teacherID):
        super().__init__(f_name_teacher, l_name_teacher)
        self.teacherID = teacherID

