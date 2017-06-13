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