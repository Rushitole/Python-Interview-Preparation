#contructor methpod
class Student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
std=Student("rushi","tole")
print(std.lname)

#lambda
x=lambda a,b:a*b
print(x(5,6))
# wrapper inyo another function
def wrapper(n):
    return lambda a:a*n
obj=wrapper(5)
print(obj(2))


#module & packages
#lamda
#constructor(__init__)
#pep8
#pythonpath (evn variable)
#Genrator 
#its a funu that return itaralble collection of item one at a time.user yield
def gen_fun():
    for i in range(1,6):
        yield i*i
obj=gen_fun()
for val in obj:
    print(val)

#Picking nd unpikling

#decorator
def deco(func):
    def inner():
        print("i'm decoartor")
        func()
    return inner
@deco
def ordinary():
    print("ordinary")
ordinary()

#break , continue pass
for i in range(10):
    if i==2:
        continue
    elif i==4:
        break
    elif i==1:
        pass
print(i)

#args and kargs
def args(*kids):
    print("yongest child :",kids[2])
args("rushi","raj","rupali")

#krargs
def kargs(c1,c2,c3):
    print("yongest child is :", c1)
kargs(c1="ram",c2="rucha", c3="rina")

#python memrory management
#PIP
#self
#django>>>
    #manage.py
    #model- referes to the class that map to database table or db connections
#django response lifecycle>>
    # settin.py >>
    #middleware >>request is now move
    #url router >>get url path from request and trid to map with url path in url.py
    #as soon as it has mapped it call to equibalent view function, from where equivalent eesponse is genrated
    # response >>middleware >>>server

#polymorphimsm >> ability  of msg to disply in more than one form.
#exeception handling >>try,except,finally
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("cod in finaly always exucute")

#loop >>while and for loop 
#map,filter reduce*
x=[12,3,4,5]
def square(x):
    return x*x
sq=map(square,x)
print(list(sq))

#filter
y=[12,16,18,19,21,22,28]
def fill(x):
    if x>=18:
        return True
adult=filter(fill,y)
print(list(adult))

# reduce
from functools import reduce
z=[2,3,4,5]
def redu(a,b):
    return a*b
result=reduce(redu,z)
print(result)

#######################################
# rev string
s="rushi"
print(s[::-1])
def rstr():
    rev=""
    for i in s:
        rev=i+rev
        return rev
print(s)

# rev int
n=321329
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

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
def deco(fun):
    def inner():
        print("func in deco")
        fun()
    return inner
@deco
def ordinary():
    print("ordinary")
ordinary()

#cmn element in the list
l1=[1,2,3,4]
l2=[3,4,5,6]
cmn=list(set(l1) & set(list(l2)))
print(cmn)

#nested list to single list
l=[1,2,[3,4],[5,6,7]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#combine 2 into 1 list
a=[1,2,3,4]
b=[5,6,7,8]
s=[(x+y) for (x,y) in zip(a,b)]
t=[(x*y) for (x,y) in zip(a,b)]
print(s,t)

#missing number in the list
l=[1,2,3,5,6,8,10]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#duplicate elemet in the list
l=[1,2,3,4,5,3,4,6,7]
d=[]
u=[]
for i in l:
    if i not in u:
        u.append(i)

    else:
        d.append(i)
print(u,d)

#occurnace of char
s="rushikesh".lower()
op={}
for i in s:
    if i in op:
        op[i]+=1

    else:
        op[i]=1

print(str(op))

#rearrage sigit
d=str(9847834)
print("".join(sorted(d,reverse=True)))
# print("".join(sorted(d,reverse=True)))


#2nd largest element
l=[12,13,19,20,5]
l.sort()
print(l[-2])

#ovel and consonent
s="rushiikesk".lower()
vovel="aeiou"
v=[]
c=[]
for i in s:
    if i.isalpha():
        if i in vovel:
            v.append(i)
        else:
            c.append(i)
print(v,c)

#sep string n int
l=["rushi","rsm","rutu",1,3,4,5]
n=[]
s=[]
for i in l:
    if type(i)==str:
        s.append(i)

    else:
        n.append(i)
print(n,s)




