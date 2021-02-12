class Parent:
    def fun1(self):
        print("I'M parent class method")
class Child(Parent):
    def fun2(self):
        print("I'm child class method")

obj1=Parent()
obj2=Child()

obj1.fun1()
obj2.fun2()