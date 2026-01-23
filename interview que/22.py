"""
#ambda
t=lambda x,y:x*y
print(t(2,4))

#break , conti & pass
list=range(8)
for i in list:
    if (i==4):
        break
    print(i)
 
lst=range(10)
for j in lst:
    if j==4:
        continue
    print(j,end="")

for j in lst:
    pass
#-----------------------------------------------------
#map filter reduce
l=[1,2,3,4,5]
y=map(lambda x:x*x,l)
print(list(y))

#filter
l1=[12,19,21,18,27,23,14,30]
z=filter(lambda a:a>=18,l1)
print(list(z))

# reduce
from functools import reduce
l2=[1,2,3,4,5]
d=reduce(lambda m,n:m*n,l2)
print(d)
#------------------------------------------------------
#encapsulation : __bal -- is private so we can't access it directly.
class Bank():
    def __init__(self,bal):
        self.__bal=bal
    def depo(self,amt):
        self.__bal+=amt
    def showb(self):
        print("C bal is : ", self.__bal)
acc=Bank(56000)
acc.depo(4000)
acc.showb()
#_________________________________________________________
#Abstarction:provide require deetails and hide implemention from the word
from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("bike started")
obj=Bike()
obj.start()
#---------------------------------------------------------------
#polymorphism
#inheritance


#iterator -- is the oject that return a element 1 by 1 using iter 
#genratror -- its an easy way  to cretate the ierator using yield funtion

#iterrator
l=[1,2,3]
it=iter(l)
print(next(it))
print(next(it))
print(next(it))

#genrat
def gen(n):
    for i in range(n):
        yield i
for j in gen(5):
    print(j)


# Decorator

def deco(fun):
    def warpper():
        print("before fun call")
        fun()
        print("after fun call")
    return warpper
@deco
def ordinary():
    print('im ordinary')
ordinary()

#args and kwargs
def args(*kids):
    print("yongest child is ",kids[2])
args("rushi","ram","ankit")

def kargs(c1,c2,c3):
    print("yongest child is",c2)
kargs(c1="rushi",c2="ramu",c3="chintu")


#try except and block
try:
    x=10/0
    print("it will not print")
except ZeroDivisionError:
    print("zero division error")
finally:          # just for cleanup code 
    print("always exucuted")



# diff for n while loop

for i in range(1,6): 
    print(i)
#----------------
i=1
while i<6:
    print(i,end="")
    i+=1

# Contractor

class Init:
    def __init__(self,name):
        self.name=name
obj=Init("rushi")
print(obj.name)
###########################################################Important Programs###################################################
# rev string & int 
s="rushikesh"
print(s[::-1])
I=1234
print(str(I)[::-1])

i=12345
rev=0
while i>0:
    digit=i%10
    rev=rev*10+digit
    i//=10
print(rev)


# pallindromee
s="Nayan"
if s.lower()==s.lower()[::-1]:
    print("pall")
else:
    print("npp")

#Fact
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

# fibo
def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
print(fibo(10))

#sencond largest element in the list
l=[1,2,3,4,5,6]
l.sort()
print(l[-2])

#decorator
def deco(fun):
    def wrapper():
        print("before fucn call")
        fun()
        print("after fun call")
    return wrapper
@deco
def ordinary():
    print("ordinary func")
ordinary()

#comman element in the list 
lst=[1,2,3,4,5,4,3,6,7]
lst1=[1,2,3,4,5,6,7]
cmn=list(set(lst)& set(list(lst1)))
print(cmn)

#odd n even 
l=[1,2,3,4,5,6]
odd=[]
evn=[]
for i in l:
    if i%2==0:
        evn.append(i)
    else:
        odd.append(i)
print(odd,evn)

#vovel in the string 
st="Zrushikesh"
ovel="aeiouAEIOU"
count=0
for i in st:
    if i in ovel:
        count+=1
print(count)

#find max producnt of 2 distinct elemet 
l=[1,2,9,3,4,7,8]
l.sort()
print(l[-2]*l[-1])

# occuring of char in the string 
str="RushikershTole".lower()
op={}
for i in str:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(op)

# nested to one
nes=[1,2,3,4,[5,6,7]]
o=[]
for i in nes:
    if isinstance(i,list):
        o.extend(i)
    else:
        o.append(i)
print(o)

a=[1,2,3]
b=[4,5,6]
d=[(x+y) for (x,y) in zip(a,b)]
print(d)

#square list 
s=[1,2,3,4]
t=map(lambda x:x*x,s)
print(list(t))
#or
m=[x**2 for x in s]
print(m)

#Duplicates elemenent in the list
l2=[1,2,3,4,5,6,7,8,5,4,3]
d=[]
u=[]
for i in l2:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(d)
print(u)



str="rushiksh"
op={}
for i in str:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(op)

#
l=[1,2,3,4,[4,5,6]]
o_p=[]
for i in l:
    if isinstance(i,list):
        o_p.extend(i)
    else:
        o_p.append(i)
print(o_p)

#encapsulation
class BankA:
    def __init__(self,bal):
        self.__bal=bal
    def depo(self,amt):
        self.__bal+=amt
    def showb(self):
        print("bal is",self.__bal)
obj=BankA(18990)
obj.depo(20000)
obj.showb()

#abstarct 
from abc import ABC ,abstractmethod
class Vehicle(ABC):
        @abstractmethod
        def start(self):
            pass
class Bike(Vehicle):
    def start(self):
        print("bike started")
obj=Bike()
obj.start()

#len of each string
l=["rushi","ram","rupam","rupali"]
x=map(lambda x:len(x),l)
print(list(x))

c=[1,2,3]
d=[5,6,7]
f=[(x*y) for (x,y) in zip(c,d)]
print(f)

#missing number in the lst
l=[1,2,3,4,6,7,9]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#sep string and number from the list
l=["r",1,"t",3,"g",43,"i",77,"pp"]
s=[]
n=[]
for i in l:
    if type(i)==str:
        s.append(i)
    else:
        n.append(i)
print(s)
print(n)        

#occurnace
str="Rushikeshtole".lower()
op={}
for i in str:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(op)

#missing nuumber in the list
l=[1,2,3,4,6,8,9]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)

print(miss)
"""
#
l=[1,2,3,4,[5,6,7],[5,8]]
op=[]
for i in l:
	if isinstance(i,list):
		op.extend(i)
	else:
		op.append(i)
print(op)
		

#reversr string without slice
def revstr(s):
	rstr=""
	for i in s:
		rstr=i+rstr
	return rstr
str="rushi"
print(revstr(str))

s="rushi"
print("".join(reversed(s)))
	
