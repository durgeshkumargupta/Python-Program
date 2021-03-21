# Method overriding
class Employee:
    raise_amt=1.04
    def __init__(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def apply_raise(self):
        self.pay=self.pay*self.raise_amt
    def display(self):
        print("First Name:",self.first)
        print("Last Name:",self.last)
        print("Employee ID:",self.empid)
        print("Pay:",self.pay)
class Developer(Employee):
    raise_amt = 1.05

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt
class Manager(Employee):
    raise_amt = 1.06

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

emp1=Manager("Durgesh","Kumar","RVCE20MCA064",50000)

emp2=Developer("Prince","Kumar","RVCE20MCA065",60000)

emp1.apply_raise()
emp2.apply_raise()
print(emp1.display())
print(emp2.display())