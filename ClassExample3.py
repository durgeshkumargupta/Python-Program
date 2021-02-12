class Sample:
    def fun1(self):
        print("I'm fun1 function")

    def fun2(self):
        self.fun1()
        print("I'm fun2 function")


obj = Sample()
obj.fun2()
obj.fun1()
