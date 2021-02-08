class Employee:

    def display(self):
        print("I am parent class")


class Department(Employee):

    def display(self):
#        super().display(self)
        print("I am child class")


dis1 = Employee()
dis1.display()

print("_______________")
dep = Department()
dep.display()
