# rev int
n=123456
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

# rev string
s="Akshayrane"
print(s[::-1])
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))

#fact
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fibo
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fib(6))

#deco
def deco(func):
    def inner():
        print("i'm decorated")
        func()
    return inner
@deco
def ordinary():
    print("o'm ordinary")
ordinary()

#cmm element in the list
l=[1,2,3,4]
l2=[3,4,5,6]
cmn=list(set(l) & set(list(l2)) )
print(cmn)

#nestedt to single list
l=[1,2,3,[4,5],[6,7]]
op=[]
for i in l:
    if isinstance (i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#combine 2 list into 1 list
a=[1,2,3,4]
b=[5,6,7,8]
s=[(x+y) for (x,y) in zip(a,b)]
# z=a.append(b)
# print(z)
print(s)

#Map filter reduce
# map fun is use to apply the same func to every item in the list & return new obj
l=[1,2,3,4]
def square(l):
    return l*l
sq=list(map(square,l))
print(sq)

# filter
l=[12,18,19,20,21,16,22]
def fill(x):
    if x>=18:
        return True
adults=list(filter(fill,l))
print(adults)

# reduce
from functools import reduce
n=[1,2,3,4]
def red(a,b):
    return a*b
y=reduce(red,n)
print(y)

# find duplicates element in the list
l=[1,2,3,4,1,3,4,5,6]
u=[]
d=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(d)

#occurance of char
s="RushikeshToler".lower()

op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(str(op))

#rearranfe digit
n=str(43646657)
print("".join(sorted(n,reverse=True)))
print("".join(sorted(n,reverse=False)))

# 2nd largest element in the list
l=[12,2,19,20,27,19,34]
l.sort()
print(l[-2])

#prime or not
a=7
if a<2:
    print("np")
else:
    for i in range(2,a):
        if a%i==0:
            print("np")
            break
    else:
        print("prime")


#ovel and consonent
# s=input("String : ").lower()
vowel="aeiou"
v=[]
c=[]
for i in s:
    if i.isalpha():
        if i in vowel:
            v.append(i)
        else:
            c.append(i)
print(v,c)


# genrator exapmple
def square_gen():
    for i in range(1,6):
        yield i*i
square=square_gen()
for val in square:
    print(val)

# break , conti nd pass
for i in range(7):
    if i==2:
        continue
    elif i==6:
        break
    elif i==1:
        pass
print(i)


#p=exeption handleimng 
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("the code under finally is always executed")

#inheritance - one class inherits the method & property of another class
#single-- child class inherits properties from parent class   a--->b
class Parent:
    def fun1(self):
        print("fun in parent class")
class Child(Parent):
    def fun2(self):
        print("fun in child class")
obj=Child()
obj.fun1()
obj.fun2()

# multiple inheritance - 1 class can be derived from more than 1 class  a,b-->c

class Father:
    def father(self):
        print(self.fathername)
class Mother:
    def mother(self):
        print(self.mothername)
class Son(Father,Mother):
    def parent(self):
        print(self.fathername)
        print(self.mothername)
obj=Son()
obj.fathername="Gajanan"
obj.mothername="Sangita"
obj.parent()


#multilevel inheritance a-->b-->c

#genrator

def square_gen():
    for i in range(1,11):
        yield i*i
s=square_gen()
for val in s:
    print(val)

#map filter reduce
#map funcation is used to apply the same function to every item in the list & and return new map object
# square of list using map

s=[1,2,3,4,5]
def square(s):
    return s*s
square_n=map(square,s)
print(list(square_n))

#filter - it filter the sequence with the help of function , test each element in the sequence is true or not
ages=[12,15,23,29,18,17,16,10]
def fun(x):
    if x>=18:
        return True
adult=filter(fun,ages)
print(list(adult))

#reduce -- reduce list of value in single unit
from functools import reduce
# n=[1,2,3,4]
# def red(a,b):
#     return a*b
# y=reduce(red,n)
# print(y)

n=[12,3,4,5]
def red(a,b):
    return a*b
y=reduce(red,n)
print(y)




