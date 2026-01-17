# #decorator
"""
# def my_deco(func):
#     def wrapper():
#         print("before func call")
#         func()
#         print("after fucn call")
#     return wrapper
# @my_deco
# def hello():
#     print("hello rushi")
# hello()

# #lambda
# x=lambda a,b:a*b
# print(x(2,4))

# #break continue & pass

# #break- useed to exit the loop permanatly when spec condition is met
# #conti: - used to skip current iterration of loop when spec contition is met and conti to next itretaion of loop
# # pass: No operation of loop

# list=range(8)
# for x in list:
#     if(x==4):
#         continue
# print(x) 

# #inheritance
# #single- child cls inherite property from parent class
# class Parent:
#     def fun1(self):
#         print(" f in parent")
# class Child(Parent):
#     def fun2(self):
#         print("f in child")

# obj=Child()
# obj.fun1()
# obj.fun2()

#map - used to apply same fun to every item in the klist  and return new mapopbaject
#squeare of each number
n=[1,2,3,4]
def square(n):
    return n*n
sq_n=map(square,n)
rslt=list(sq_n)
print(rslt)

m=[1,2,3,4]
r=map(lambda x:x*x,m)
print(list(r))

#filter - filter the given sq
ages=[21,19,11,23,13,20,15]
evn=list(filter(lambda x:x>=18,ages))
print(evn)

#reduce- combine all elements of a list into onee single value
from functools import reduce
nums=[1,2,3,4]
result=reduce(lambda a,b:a+b,nums)
print(result)

#try except block
try:
    r=10/0
    print("this will not print")
except ZeroDivisionError:
    print("error")
finally:
    print("this will always print")


lst=[1,2,3,[4,5]]
op=[]
for i in lst:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)


#Revrse staing 
x="Nayan"
print(x[::-1])
y=12345
print(str(y)[::-1])

#palindrome
if x.lower()==x.lower()[::-1]:
    print("p")
else:
    print("np")

#2nd largeest element from list
l=[1,3,4,56,7,78]
l.sort()
print(l[-2])

#decorator with example
def deco(func):
    def inner():
        print("before fucn call")
        func()
        print("after fucn call")
    return inner
@deco
def ordinary():
    print("ordi func")

ordinary()

#find comman element in the list
l=[1,2,3]
l1=[4,5,6,3]
cmn=list(set(l) & set(list(l1)))
print(cmn)

#odd and even number
def is_even(n):
    return n%2==0
print(is_even(4))

#fact
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

# count the numbetr of uppercase letter in string 
def upper(n):
    return sum(1 for char in n if char.isupper())
print(upper("Rushi"))

#single inhertitance - child class acces properties from parent class
class Parent:
    def fun1(self):
        print("parente class")
class Child(Parent):
    def fun2(self):
        print("child class")
obj=Child()
obj.fun1()
obj.fun2()

#find the poduct of 2 distict element 
l=[10,20,30,40,50]
def maxp(l):
    l.sort()
    return l[-1]*l[-2]
print(maxp(l))

# revrese int without using convert into string
n=1234
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

# print 1-100
for i in range(101):
    print(i)

l=[1,2,3,4,[5,6]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#duplicate and unique number in the list
l=[1,2,3,3,4,2,5,6,7,5,8]
u=[]
d=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(u)
print(d)

#combine 2 list into 1
a=[1,2,3,4]
b=[5,6,7,8]
z=[(x+y) for (x,y) in zip(a,b)]
print(z)

#square list
l=[1,2,3,4]
sq=[x**2 for x in l]
print(sq)

#occurnace of char in the string
s="rushikesh"
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(str(op))

#missing number in the list
l=[1,2,3,4,5,6,7,10]
m=[]
for i in range(l[0],l[-1]):
    if i not in l:
        m.append(i)
print(m)

""" 

#sep striing n int from list
l=[1,2,"r",3,"s",4,"m","t",5]
s=[]
n=[]
for i in range(0,len(l)):
    if str(l[i]).isdigit():
        n.append(l[i])
    else:
        s.append(l[i])
print(n,s)