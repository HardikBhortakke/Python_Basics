class Person(object):
    def __init__(self, name):
        self.name = name
 
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False
 

class Employee(Person):
    def __init__(self, name):
        super().__init__(name)

    def isEmployee(self):
        return True
 
 
if __name__=='__main__':
    emp = Person("Joanna")  # An Object of Person
    print(emp.getName(), emp.isEmployee())
    
    emp = Employee("Peter")  # An Object of Employee
    print(emp.getName(), emp.isEmployee())