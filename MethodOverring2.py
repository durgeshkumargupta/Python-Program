class Parent:
    def sum(self, a, b):
        print("Sum of two variable of Parent class:", a + b)


class Child(Parent):
    def sum(self, a, b):
        super().sum(a,b)
        print("Sum of two variable child class:", a + b)


obj1 = Parent()
obj1.sum(11, 22)
print("_______________")

obj2 = Child()
obj2.sum(55, 5)
