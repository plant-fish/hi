class C:
    def get_self(self):
        print(self)

        
c = C()
c.get_self()

c

C.get_self(c)

d = C()
d.x = 250
d.x

c.x

c.x = 250
c.x

d.x

c.__dict__

d.__dict__

d.y = 660
d.__dict__

class C:
    def set_x(self,v):
        self.x=v

        
c = C()
c.__dict__

c.set_x(250)
c.__dict__

c.x

class C:
    x = 100
    def set_x(self,v):
        x = v

        
c = C()
c.set_x(250)
c.x

C.x

C.x = 250
c.x

250
c.__dict__
{}
c.y
##
class C:
    pass

C.x = 250
C.y = "fish"
C.z = [1,2,3]
print(C.x)
250
print(C.y)
fish
print(C.z)
[1, 2, 3]
##
d = {}
d['x'] = 250
d['y'] = "fish"
d['z'] = [1,2,3]
print(d['x'])
250
print(d['y'])
fish
print(d['z'])
[1, 2, 3]
class C:
    pass

c = C()
c.x = 250
c.y = "fish"
c.z = [1,2,3]
