3 + 5
3 * 5
"Py" + "Fish\C"
"FishC" * 3
len("FishC")
len(["FishC","Python","Me"])
len({"name":"hi","age":18})

class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

class Square(Shape):
    def __init__(self,length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self,radius):
        super().__init__("圆形")
        self.length = radius
    def area(self):
        return self.length * self.length * 3.14

class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__("三角形")
        self.base = base
        self.height = height
    def area(self):
        return self.base *self.height / 2

s = Square(5)
c = Circle(6)
t = Triangle(3,4)
print(s.name)
print(c.name)
print(t.name)
print(c.area())
print(s.area())
print(t.area())
    
#
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"I am a Cat called{self.name},{self.age}")
    def say(self):
        print("ha")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"called{self.name}dog,{self.age}")
    def say(self):
        print("wuwu")

c = Cat("web",4)
d = Dog("Great",7)
def animal(x):
    x.intro()
    x.say()

animal(c)
animal(d)

class Bicycle:
    def intro(self):
        print("gogogog")
    def say(self):
        print("heiehie")

b = Bicycle()
animal(b)
