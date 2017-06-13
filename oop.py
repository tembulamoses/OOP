"""This is an oop representation of a typical school in 
kenya (and by extension beyond) other the special school
"""
from abc import ABCMeta, abstractmethod

class SchoolMember:
    '''Represents any school member.'''
    __metaclass__ = ABCMeta

    age_description = 'minor'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        '''Tell my details.'''
        return 'Member Type: {}'.format(self.member_type()), 'Name:"{}" Age:"{}" Description:"{}"'.format(self.name, self.age, self.age_description)

    
    @abstractmethod
    def member_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass




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
t = Teacher('alphayo', 30, 1000)

l = [s, t]

for member in l:
    print(member.detail())