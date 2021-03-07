class Student:
    def __init__(self, usn=0, name=0, age=0,sem=0):
        pass
    def getData(self):
        self.name = input("Enter Name:")
        self.usn = input("Enter USN:")
        self.age = int(input("Enter age:"))
        self.sem = int(input("Enter sem:"))
class Derived1(Student):
    def __init__(self,m1=0,m2=0,m3=0,m4=0,m5=0):
        pass
    def Subject_marks(self):
        s=Student()
        s.m1=int("Enter First Marks:")
        s.m2 = int("Enter Second Marks:")
        s.m3 = int("Enter third Marks:")
        s.m4 = int("Enter Fouth Marks:")
        s.m5 = int("Enter five Marks:")
class Derived2(Derived1):
    def display(self):
        total=self.m1+self.m2+self.m3+self.m4+self.m5
        per=total%500*100
        print("Name:",self.name)
        print("USN:",self.usn)
        print("Semester:",self.sem)
        print("Total marks:",total)
        print("Percentage:",per)
obj=Derived2()
obj.display()