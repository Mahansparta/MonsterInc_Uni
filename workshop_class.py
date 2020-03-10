
class Workshop():
    def __init__(self, subject, teacher, attendees=[]):
        self.subject = subject
        self.teacher = teacher
        self.list_of_attendees = [attendees]


    #
    # def make_workshop(self):
    #     the_workshop = []
    #     the_workshop.append(self.subject)
    #     the_workshop.append(self.teacher)
    #     the_workshop.append(self.list_of_attendees)
    #     return the_workshop