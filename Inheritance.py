#Inheritance
class Person:
    def __init__(self):
        self.__first= None
        self.__last = None
        self.__name = None
        self.__address = None
        self.__phno = 0
        
    def set_per(self):
        self.__first= input('Enter First Name:')
        self.__last = input('Enter Last Name:')
        self.__name = self.__first+' '+self.__last
        self.__address = input('Enter Address:')
        self.__phno = int(input('Enter Phone no:'))
        
    def get_per(self):
        print('Name: ',self.__name)
        print('Address: ',self.__address)
        print('Phone No: ',self.__phno)
    
    def first(self):
        return self.__first
        
    def last(self):
        return self.__last

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.__id = 0
        self.__sal = 0
        self.__email = None

    def set_emp(self):
        self.__id = int(input('Enter Emp Id: '))
        self.__sal = int(input('Enter Emp Salary: '))
        self.__email = self.first()+'.'+self.last()+'@email.com'

    def get_emp(self):
        print('Emp Id: ',self.__id)
        print('Salary: ',self.__sal)
        print('Email: ',self.__email)

emp = []    #Empty List
n = int(input('Enter the number of Employees:'))
for i in range(n):
    emp.append(Employee())
    emp[i].set_per()
    emp[i].set_emp()
    
print('Employee Information....')
for i in range(n):
    emp[i].get_per()
    emp[i].get_emp()
