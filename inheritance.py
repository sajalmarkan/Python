class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):
        print(f"The name of the employee is {self.name}\nId of the employee is {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")
    
e1= Employee("Sajal",24)
e1.showDetails()
e2= Programmer("Sam",24)
e2.showLanguage()