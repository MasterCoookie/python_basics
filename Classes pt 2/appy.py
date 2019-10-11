class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1


    #"normal" method does stuff in a class, takes self as an argument
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    #classmethods take a class as an argument and work on a class itself as an argument rather than an istance
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #may also be used as alternative consstructors
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    #static methods are used when we have a functions somehow associated with the class,
    #but we dont need its arguments (properties). It doesnt take self/cls
    @staticmethod
    def is_workday(day):
        if day.weekday() < 5:
            return True
        return False

    #magic mehtods
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())




    


#class inheritance
class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())






dev_1 = Developer('Jan', 'Kocurek', 50000, 'Python')
dev_2 = Developer('Kan', 'Jocurek', 60000, 'Java')
dev_1.apply_raise()
print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 70000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

Employee.set_raise_amt(1.05)
print(Employee.raise_amount)

emp_str_3 = 'Adam-Nowak-45000'

emp_3 = Employee.from_string(emp_str_3)
print(emp_3.fullname())

import datetime
mydate = datetime.date(2019, 5, 8)
print(Employee.is_workday(mydate))

print(dev_1)
print(dev_1 + dev_2)
print(len(dev_1))
