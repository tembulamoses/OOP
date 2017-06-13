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

s = Teacher('swaroop', 30, 7500)
t = Teacher('alphayo', 39, 8200)
k = Teacher('Assumpta', 31, 7000)
m = Teacher('John', 32, 8000)

l = [s, t, k,m]

for member in l:
    print(member.detail())