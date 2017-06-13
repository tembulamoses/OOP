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


s = Student('swaroop', 20, 75)
t = Student('alphayo', 19, 82)
k = Student('Assumpta', 21, 70)
m = Student('John', 22, 80)

l = [s, t, k,m]

for member in l:
    print(member.detail())
