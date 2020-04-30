#Aggregation
class Student:
    def __init__(self):
        self.__name = None
        self.__rollno = 0
        self.__marks = []
        self.__total = 0
        self.__avg = 0.0
    def setinfo(self):
        self.__name = input('Enter Name: ')
        self.__rollno = int(input('Enter Roll No: '))
        self.__marks = map(int,input('Enter Marks').split())
        self.__total = sum(self.__marks)
        self.__avg = self.__total/5
    def getinfo(self):
        print('Student Name: ',self.__name)
        print('Student Roll No: ',self.__rollno)
        print('Total: ',self.__total)
        print('Average: ',self.__avg)

class College:
    def __init__(self,other):
        self.__dept = None
        self.__sem = None
        self.__year = 0
        self.__stu = other
    def set_college(self):
        self.__stu.setinfo()
        self.__dept = input('Enter Department: ')
        self.__sem = input('Enter Semester: ')
        self.__year = input('Enter Year: ')
    def get_college(self):
        self.__stu.getinfo()
        print('Department: ',self.__dept)
        print('Year: ',self.__year)
        print('Semester: ',self.__sem)

stu = Student()
col = College(stu)
col.set_college()
col.get_college()
del col
stu.getinfo()
