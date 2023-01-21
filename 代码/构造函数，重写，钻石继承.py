class C :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y
c = C(2,3)
c.add()
5
c.mul()
6
c.__dict__

d.__dict__

d = C(4,5)
d.__dict__

d.add()

d.mul()

class D(C):
    def __init__(self,x,y,z):
        C.__init__(self,x,y)
        self.z = z
    def add(self):
        return C.add(self) + self.z
    def mul(self):
        return C.mul(self) * self.z

    
d = D(2,3,4)
d.add()

d.mul()
##
class A:
    def __init__(self):
        print("你认为邓布利多会为你哀悼吗")

        
class B1(A):
    def __init__(self):
        A.__init__(self)
        print("我是纽特")

        
class B2(A):
    def __init__(self):
        A.__init__(self):
            

class B2(A):
    def __init__(self):
        A.__init__(self)
        print("我是格")

        

class C(B1,B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("谁是邓布利多最喜欢的人")

        
c = C()
##
class B1(A):
    def __init__(self):
        super().__init__()
        print("我是纽特")

        
class B2(A):
    def __init__(self):
        super().__init__()
        print("我是格")

        
class C(B1,B2):
    def __init__(self):
        super().__init__()
        print("谁是邓布利多最喜欢的人")

        
c = C()

C.mro()

B1.mro()

C.__mro__

B2.__mro__

