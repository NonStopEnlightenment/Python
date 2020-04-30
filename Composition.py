class Date:
    def __init__(self):
        self.__day = 0
        self.__mon = 0
        self.__yr = 0
    def set_date(self):
        self.__day = int(input('Enter Day in DD Format: '))
        self.__mon = int(input('Enter Mon in MM Format: '))
        self.__yr = int(input('Enter Day in YYYY Format: '))
    def get_date(self):
        print(f'{self.__day} / {self.__mon} / {self.__yr}')

class Person:
    def __init__(self):
        self.__first= None
        self.__last = None
        self.__address = None
        self.__name = None
        self.__phno = 0
        self.__dob = Date()       #Composition (has - a relatioship)

    def set_per(self):
        self.__first= input('Enter First Name:')
        self.__last = input('Enter Last Name:')
        self.__name = self.__first+' '+self.__last
        self.__address = input('Enter Address:')
        self.__phno = int(input('Enter Phone no:'))
        self.__dob.set_date()
        
    def get_per(self):
        print('Name: ',self.__name)
        print('Address: ',self.__address)
        print('Phone No: ',self.__phno)
        print('Date of Birth')
        self.__dob.get_date()

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
        self.__doj = Date()             #Composition (has - a relatioship)

    def set_emp(self):
        self.__id = int(input('Enter Emp Id: '))
        self.__sal = int(input('Enter Emp Salary: '))
        self.__email = self.first()+'.'+self.last()+'@email.com'
        self.__doj.set_date()

    def get_emp(self):
        print('Emp Id: ',self.__id)
        print('Salary: ',self.__sal)
        print('Email: ',self.__email)
        print('Date of Joining')
        self.__doj.get_date()
        
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
