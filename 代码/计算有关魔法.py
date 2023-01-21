class S(str):
    def __add__(self,other):
        return len(self) + len(other)

s1 = S("FishC")
s2 = S("Python")
print(s1 + s2)
print(s1 + "Python")
print("FishC" + s2)

##
class S1(str):
    def __add__(self,other):
        return NotImplemented

class S2(str):
    def __radd__(self,other):
        return len(self) + len(other)

s1 = S1("Apple")
s2 = S2("Banana")
print(s1 + s2)
s1 += s2
print(s1)
type(s1)
s2 += s2
print(s2)
type(s2)

##
class ZH_INT:
    def __init__(self,num):
        self.num = num
    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            zh = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8}
            result = 0

            for each in self.num:
                if each in zh:
                    result += zh[each]
                else:
                    result += int(each)
                result *= 10

            return result // 10
n = ZH_INT("520")
print(int(n))
n = ZH_INT(3.14)
print(int(n))
n = ZH_INT("五二一")
print(int(n))
n = ZH_INT("五二一314")
print(int(n))

##
