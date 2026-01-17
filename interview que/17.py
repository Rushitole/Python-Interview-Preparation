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
# class BankA:
#     def __init__(self,bal):
#         self.bal=bal   # private variavble
#     def depo(self,amt):
#         self.bal += amt    
#     def showb(self):
#         print("bal:", self.bal)
# acc=BankA(1000)
# acc.depo(500)
# acc.showb()
  


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