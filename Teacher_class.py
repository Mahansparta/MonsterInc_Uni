from Monster_class import *

class Teacher(Monster):

    def __init__(self, f_name, l_name, teacherID):
        super().__init__(f_name, l_name)
        self.teacherID = teacherID

