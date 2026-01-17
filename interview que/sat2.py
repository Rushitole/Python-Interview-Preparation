# missing interger ]
l=[1,2,3,4,7,8,9]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#seprat sting n integer
l=["r","d","t",3,5,7,"y"]
s=[]
n=[]
for i in l:
    if type(i)==str:
       s.append(i)
    else:
       n.append(i)
print(s,n)

#ovel n consonnet
s="rusjiksh".lower()
vowel="aeiou"
c=[]
v=[]
for i in s:
    if i.isalpha():
        if i in vowel:
            v.append(i)
        else:
            c.append(i)
print(v,c)

#nrsted list to 1
l=[1,2,[3,4],[5,6]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#fibo series
def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fibo(5))

#fact
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#deco
def deco(func):
    def inner():
        print("im decorator")
        func()
    return inner
@deco
def ordinary():
    print("ordinary")
ordinary()

#rev string 
s="rushikesh"
print(s[::-1])
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))

# rev integer
n=23479874897
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

#combine 2 llist to 1
l1=[1,2,3,4]
l2=[5,6,7,8]
s=[(x+y) for (x,y) in zip(l1,l2)]
print(s)

#map 
l=[1,2,3,4]
def square(l):
    return l*l
square_n=map(square,l)
print(list(square_n))

#filter 
l=[12,23,18,23,10,18,16]
def fill_n(x):
    if x>=18:
        return True
adult=filter(fill_n,l)
print(list(adult))

# reduce
from functools import reduce
l=[1,2,3,3,4]
def red(a,b):
    return a*b
v=reduce(red,l)
print(v)

#eduplicate eleement in the list
l=[1,2,3,4,4,5,3,6]
d=[]
u=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(u,d)

#occurance oc char
s="rushikesh".lower()
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(op)

#prime or not
a=9
if a<2:
    print("np")
else:
    for i in range(2,a):
        if a%i==0:
            print("np")
            break
    else:
        print("p")
#ovel
s="rushikesh".lower()
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

#single inheritance
class  Parent():
    def fun1(self):
        print("f in p")

class Child(Parent):
    def fun2(self):
        print("f in c")
obj=Child()
obj.fun1()
obj.fun2()

#genrator
def gen_s():
    for i in range(1,6):
        yield i*i
square=gen_s()
for val in square:
    print(val)

#break continue pass
for i in range(10):
    if i==2:
        continue
    elif i==5:
        break
    elif i==3:
        pass
print(i)

#exeption
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("always excuted")


