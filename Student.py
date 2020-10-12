# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    
    def set_gender(self, gender):
        #if self.__gender == 'F' or 'female' or 'Female':
        self.__gender = gender
    
    def get_gender(self):
        if self.__gender == 'F' or 'female' or 'Female' or '女':
            print('女')

if __name__ == '__main__':
    lisa = Student('Lisa', 'female')
    lisa.get_gender()
    lisa.set_gender('F')
    lisa.get_gender()