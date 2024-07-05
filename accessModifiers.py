#private access modifier
class Employee:
    def __init__(self):
        self.__name="Sam"
        self.__id=1
    
    def showDetails(self):
        print(f"The name of the employee is {self.name}\nId of the employee is {self.id}")
    
a= Employee()
# print(a.__name,a.__id) Cannot use directly because it is private attribute

print(a._Employee__name,"\n",a._Employee__id)

#Protected

class Student:
    def __init__(self):
        self._name = "Sajal"

    def _funName(self):
        return "Enjoying Python"
    
class Subjects(Student):
    pass

a = Student()
a1 = Subjects()

print(a._name)
print(a._funName())

print(a1._name)
print(a1._funName())
