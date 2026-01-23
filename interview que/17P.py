# #lamda:
# x=lambda a,b:a*b
# print(x(2,3))

# #map
# l=[1,2,3,4,5,6]
# y=map(lambda x:x*x,l)
# print(list(y))

# #filter
# lst=[21,20,15,14,13,22,28]
# adult=filter(lambda x:x>=18,lst)
# print(list(adult))

# #reduce
# from functools import reduce
# l1=[2,3,4,5,6]
# res=reduce(lambda x,y:x*y,l1)
# print(res)

#explain this with example
#ploymorphism
#encapsulation
#abstarction
#inheritance  

#polymorphisam: 
#encapsulation : bind data(var) & method (function) in one class and hiding data from direct access to keep it safe.
class BankA:
    def __init__(self,bal):
        self.__bal=bal
    def depo(self,amt):
        self.__bal+=amt
    def Showb(self):
        print("bal", self.__bal)
acc=BankA(2000)
acc.depo(7700)
acc.Showb()

#abstarction : it hide the internal details and show only nessaey info
from abc import ABC ,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("bike started")
A=Bike()
A.start()

#inheritance
#Single : 
# class Father:
#     def Fun(self):
#         print ("f in father class")
# class Child(Father):
#     def fun2(self):
#         print("fun in child cls")
# obj=Child()
# obj.Fun()
# obj.fun2()

#Multiple - 1,2-->3
# class Father:
#     def father(self,fname):
#         self.fname=fname
# class Mother:
#     def mother(self,mname):
#         self.mname=mname
# class Son(Father,Mother):
#     def parent(self):
#         print (self.fname)
#         print(self.mname)
# obj=Son()
# obj.fname="gjanan"
# obj.mname="sangita"
# obj.parent()

#Multilevel -gf--f--s

class Grandfather:
    def __init__(self,gfname):
        self.gfname=gfname

class Father(Grandfather):
    def __init__(self,fname,gfname):
        self.fname=fname
        super().__init__(gfname)
class Son(Father):
    def __init__(self,sname,fname,gfname):
        self.sname=sname
        super().__init__(fname,gfname)

    def pname(self):
        print (self.gfname)
        print (self.fname)
        print (self.sname)
obj=Son("rushi","gajana","tulshiram")
obj.pname()




#decorator
def deco(fun):
    def wrapper():
        print("before call")
        fun()
        print("after call")
    return wrapper
@deco
def ordinary():
    print("ordi")
ordinary()     













