from school_member import SchoolMember

class Teacher(SchoolMember):
    '''Represents a teacher.'''

    age_description = 'Adult'

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def member_type(self):
        return 'Teacher'

    def detail(self):
        
        return SchoolMember.detail(self), 'Salary: "{:d}"'.format(self.salary)

s = Student('swaroop', 20, 75)
t = Student('alphayo', 19, 82)
k = Student('Assumpta', 21, 70)
m = Student('John', 22, 80)

l = [s, t, k,m]

for member in l:
    print(member.detail())