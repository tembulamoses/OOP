from school_member import SchoolMember
class Student(SchoolMember):
    '''Represents a student.'''
    
    age_description = 'minor'
    
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def member_type(self):
        return 'Student'    

    def detail(self):
        return SchoolMember.detail(self), 'Marks: "{:d}"'.format(self.marks)