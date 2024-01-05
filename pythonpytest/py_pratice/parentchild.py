class parent:
    def __init__(self,name):
        self.name=name
        print("parent")

class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child")
    def disply(self):
        print(self.name)
        print(self.age)

c1 = child("mahendra",35)
print(c1.disply())


