class Student:
    name=""
    roll=0
    marks=0
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)

obj=Student("Durgesh",21,88)
obj.display()