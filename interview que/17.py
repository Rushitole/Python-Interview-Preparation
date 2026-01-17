# #lambda -
# x= lambda a,b:a*b
# print(x(2,3))

# #break continue and pass
# #use to exit loop permently when specific confition is met.
# list=range(8)
# for x in list:
#     if(x==4):
#         break
# print(x)
# #
# #continue- use to tp oexit loop when specific condtion is met and continue with next iteration of loop
# lst=range(10)
# for i in lst:
#     if i==8:
#         continue
# print(i)

# #pass- nop opration statemnet

# #Iteratror- its an ojject that return a element one by one using iter
# num=[12,3,4]
# it=iter(num)
# print(next(it))
# print(next(it))
# print(next(it))

# #Genrator: its an easy way to create an iterator using yield.
# def gen():
#     yield 1
#     yield 2
# g=gen()
# print(next(g))

# def number():
#     for i in range(1,4):
#         yield i
# for x in number():
#     print(x)

#polymorphism:  the ability of mesage to disply in more than one form
x=[1,2,3]
print(len(x))
print(len("rushi"))

#encapsulation : warpping data(variable) & method (fucntion) into class and hiding the data from direct access to keep it safe.
class BanA:
    def __init__(self,bal):
        self.__bal=bal
    def depo(self,amt):
        self.__bal+=amt
    def showb(self):
        print("bal:",self.__bal)
acc=BanA(5000)
acc.depo(3000)
acc.showb()

#abstarction: hiding implemantion and shwoing only functionality
from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("Bike started")
b=Bike()
b.start()

#for loop- we know how many time to repeat it
# while- don't know how many time to repeat it

#inheritance:
#single - child class access the properties of parent class
#multiple- a class derived from more than one class
#multilevel- base class and derived class also inheritated from new derived class
#Hirarchical inheritance- more than one derived class crreated from single base class
#hybrid inheritance- multiple type of inheritance

#simgle
class Parent():
    def fun(func):
        print("fun in p")
class Child(Parent):
    def fun2(self):
        print("fucn in child class")
obj=Child()
obj.fun()
obj.fun2()

#multiple
# class Father():
#     def father(self):
#         print(self.fname)
# class Mother():
#     def mother(self):
#         print(self.mname)
# class Son(Father,Mother):
#     def parent(self):
#         print(self.fname)
#         print(self.mname)
# obj=Son()
# obj.fname="gajana"
# obj.mname="sangita"
# obj.parent()

#Multilevel
class Grandfather:
    def __init__(self,gfname):
        self.gfname=gfname

class Father(Grandfather):
    def __init__(self,fname ,gfname):
        self.fname=fname
        # Grandfather.__init__(self,gfname)
        super().__init__(gfname)
class Son(Father):
    def __init__(self,sname,fname,gfname):
        self.sname=sname
        # Father.__init__(self,fname,gfname)
        super().__init__(fname,gfname)


    def pname(self):
        print(self.gfname)
        print(self.fname)
        print(self.sname)
obj=Son("Rushi","Gajanan","Tulshiram")
# print(obj.gfname)
obj.pname()

#Hirerchical inheritance
class Parent:
    def fun1(self):
        print("f in parent class")
class Child1(Parent):
    def fun2(self):
        print("fun in child clss")
class Child2(Parent):
    def fun3(self):
        print("fucn3 in child clss")
obj1=Child1()
obj2=Child2()

obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun3()