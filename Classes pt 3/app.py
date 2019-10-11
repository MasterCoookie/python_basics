class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    #setter - a method thats sets data 
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    #deleter - just deletes data from object when called by 'del'
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    

emp_1 = Employee('Jan', 'Kocurek', 50000)

emp_1.fullname = 'Kan Jocurek'

#del emp_1.fullname

print(emp_1.fullname)