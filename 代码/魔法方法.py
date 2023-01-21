class Capstr(str):
    def __new__(cls,string):
        string = string.upper()
        return super().__new__(cls,string)

cs = Capstr("FishC")
print(cs)
cs.lower()
print(cs)
print(cs.capitalize())
class C:
    def __init__(self):
        print("come")
    def __del__(self):
        print("go")

c = C()

del c
###
class D:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        global x
        x = self

d = D("zoey")
print(d)
print(d.name)
del d
##再print d报错##
print(x)
print(x.name)

###
class E:
    def __init__(self,name,func):
        self.name = name
        self.func = func
    def __del__(self):
        self.func(self)

def outter():
    x = 0
    def inner(y=None):
        nonlocal x
        if y:
            x = y
        else:
            return x
    return inner
f = outter()
e = E("fish",f)
print(e)
print(e.name)
del e
##prin e报错##
g = f()
print(g)
print(g.name)
