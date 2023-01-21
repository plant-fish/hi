class C:
    def __init__(self,x):
        self._x = x
    def set_x(self,x):
        self._x = x
    def get_x(self):
        print(self._x)

c = C(250)
c.get_x()
c.set_x(520)
print(c.get_x())
print(c.__dict__)

#
class D:
    def __func(self):
        print("Helloworld")

d = D()
d._D__func()
c.__y = 250
print(c.__dict__)

##
class C:
    def __init__(self,x):
        self.x = x

c = C(250)
print(c.x)
c.__dict__
c.y = 520
c.__dict__
c.__dict__['z'] = 666
c.__dict__
c.z
class C:
    __slots__ = ["x","y"]
    def __init__(self,x):
        self.x = x

c = C(250)
print(c.x)
c.y = 520
print(c.y)
##c.z报错##
class D:
    __slots__ = ["x","y"]
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

##d = D(3,4,5)报错##
class E(C):
    pass

e = E(250)
print(e.x)
e.y = 520
print(e.y)
e.z = 666
print(e.__slots__)
print(e.__dict__)

    
