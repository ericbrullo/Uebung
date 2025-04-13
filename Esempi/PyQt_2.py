class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self.getname()
        print("objekt:", self.name) 

    def getname(self):
        print("My name is:", self.name)


p1 = Person("Hans", 20)
p2 = Person("Peter", 30) 