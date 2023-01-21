class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print(f"I called{self.name},{self.age}years old now.")

class FlyMixin:
    def fly(self):
        print("I can fly")

class Pig(FlyMixin,Animal):
    def special(self):
        print("I can run")

p = Pig("hho",5)
p.say()
p.special()
p.fly()
##
class Displayer:
    def display(self,message):
        print(message)

class LoggerMixin:
    def log(self,message,filename="logfile.txt"):
        with open(filename,"a") as f:
            f.write(message)

    def display(self,message):
        super().display(message)
        self.log(message)

class MySubClass(LoggerMixin,Displayer):
    def log(self,message):
        super().log(message,filename="subclasslog.txt")

subclass = MySubClass()
subclass.display("This is a test.")
MySubClass.mro()
