"""lambda -
x= lambda a,b:a*b
print(x(2,3))
#***********************************************************************************************************************
#break continue and pass
#use to exit loop permently when specific confition is met.
list=range(8)
for x in list:
    if(x==4):
        break
print(x)
#
#continue- use to tp exit loop when specific condtion is met and continue with next iteration of loop
lst=range(10)
for i in lst:
    if i==8:
        continue
print(i).......................................






#pass- nop opration statemnet

#***********************************************************************************************************************

#Iteratror- its an object that return a element one by one using iter
num=[12,3,4]
it=iter(num)
print(next(it))
print(next(it))
print(next(it))

#Genrator: its an easy way to create an iterator using yield.
def gen():
    yield 1
    yield 2
g=gen()
print(next(g))

def number():
    for i in range(1,4):
        yield i
for x in number():
    print(x)
#***********************************************************************************************************************

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
#***********************************************************************************************************************

#for loop- we know how many time to repeat it
# while- don't know how many time to repeat it

#******************************************************inheritance & Types*****************************************************************

#inheritance:
#single - child class access the properties of parent class
#multiple- a class derived from more than one class
#multilevel- base class and derived class also inheritated from new derived class
#Hirarchical inheritance- more than one derived class created from single base class
#hybrid inheritance- multiple type of inheritance.

#single
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
class Father():
    def father(self):
        print(self.fname)
class Mother():
    def mother(self):
        print(self.mname)
class Son(Father,Mother):
    def parent(self):
        print(self.fname)
        print(self.mname)
obj=Son()
obj.fname="gajana"
obj.mname="sangita"
obj.parent()

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

obj1.fun1()  #parent method
obj1.fun2()  # child1 method
obj2.fun1()  #prent method
obj2.fun3()  #child 2 method

#Hybrid inheritance
class A:
    def funA(self):
        print("A class")
class B(A):            #multilevel
    def funB(self):
        print("B class")
class C(A):            #hirarchicle
    def funC(self):
        print("C class")
class D(B,C):           #Multiple inheritance
    def funD(self):
        print("D class")

obj=D()
obj.funA()
obj.funB()
obj.funC()
obj.funD()
"""
#
#*******************************************************Map, filter & reduce****************************************************************
#Higher order functions Map , filetr and reduce

#Map: Use to apply same function to every item in the list and given new map object
#squarr of each number
n=[1,2,3,4]
t=map(lambda x:x*x,n)
print(list(t))

#filetr :filter the element
m=[21,22,23,19,15,13]
ad=filter(lambda x:x>=18,m)
print(list(ad))

#Reduce:combine all elemnt in the list in single value
from functools import reduce
o=[1,2,3,4,5]
fill=reduce(lambda a,b:a+b,o)
print(fill)


#**************************************************Exception Handaling*********************************************************************
#Try : It contain the code that monitor the error or exexption or might be raised exception
#except: If any error occur in try block  then except block is exucutes (need to specify type of expection)
#Finally : no matter edxpetion occur or not Finally block ios exututed
try: 
    result=10/0
    print("this will not printed")
except ZeroDivisionError:
    print("Error : Divison bye zero")
finally:
    print("alwasy exucute")

#**************************************************Exception Handaling*********************************************************************
-