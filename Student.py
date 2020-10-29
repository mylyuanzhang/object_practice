# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def set_gender(self, gender):
        #if self.__gender == 'F' or 'female' or 'Female':
        self.gender = gender
    
    def get_gender(self):
        if self.gender == 'F' or 'female' or 'Female' or '女':
            print('女')
    
    def get_name(self):
        print(self.name)

class Lisa(Student):
    def __init__(self):
        self.name = 'Lisa'
        self.gender = 'Female'
    
    def get_gender(self):
        print('Lisa\'s gender is female')
    

if __name__ == '__main__':
    lisa = Lisa()
    lisa.get_name()
    # lisa.set_gender('F')
    lisa.get_gender()
    print(isinstance(lisa, Lisa))
    print(type(lisa))