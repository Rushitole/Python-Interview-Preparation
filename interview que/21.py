# class Dev:
#     def __init__(self,fname):
#         self.fname=fname
#     def intro(self):
#         print(self.fname)
# emp=Dev("rushi")
# emp.intro()    

# #break continue pass
# lst=range(8) 
# for i in lst:
#     if (i==4):
#         break
#     print(i)

# #continue - skip 
# lst1=range(8)
# for j in lst1:
#     if j==6:
#         continue
#     print(j)

# # args and kwargs
# def fun(*kids):
#     print("yongest child is", kids[2])
# fun("rushi","chiku","piku")

# #kwargs
# def fun1(c1,c2,c3):
#     print("young chils is", c3)
# fun1(c1="rushi",c2="golu",c3="rahi")

# #self- using this keyword you can access attribute and method of class
# #ierator -- its an object that return element in one bye one
# num=[10,20,39]
# it=iter(num)
# print(next(it))

# #genrator- its an easy way to create ierator using yield                                                         
# def gen(n):
#     for i in range(n):
#         yield i
# for num in gen(5):
#     print(num)


def fun(*kids):
    print("young child is",kids[1])
fun("rushi","chiku","rupa")

def fun1(c1,c2,c3):
    print("young boy",c3)
fun1(c1="rushi",c2="rupa",c3="ankit")

#encapsulation - bundle data(attribute) & method (function) that operate in data within simgle unit contraol access and 
#                protecting the internal state of on object.
class Bank:
    def __init__(self,bal):
        self.__bal=bal
    def depo(self,amt):
        self.__bal+=amt
    def showb(self):
        print("total bal",self.__bal)
obj=Bank(50000)
obj.depo(20000)
obj.showb()

#Abstaction - hoding implemention and showing only funality
from abc import ABC , abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("bike started")
b=Bike()
b.start()

#try except block

try:
    n=10/0
    print("this will not print")
except ZeroDivisionError:
    print("zerodivision Error")
finally:
    print("alwsy exucuted")


