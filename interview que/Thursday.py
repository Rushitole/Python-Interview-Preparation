## rev int
n=128432789
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

# rev string
s="shailesh"
print(s[::-1])
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))

# fact
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fabo series
def fab(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fab(10))

#missing number in the list
l=[1,2,3,5,7,9,10]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#decoratorr
def deco(func):
    def inner():
        print("i'm deco")
        func()
    return inner
@deco
def ordinay():
    print("i'm ordinary")
ordinay()

#cmn element in the list
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
cmn=list(set(l1)& set(list(l2)))
print(cmn)

#nested to single list
l=[1,2,[3,4,5],[6,7,8]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#combine 2 list to 1
a=[1,2,3,4,5]
b=[5,6,7,8,9]
s=[(x+y) for (x,y) in zip(a,b)]
t=[(x*y) for (x,y) in zip(a,b)]

print(s,"",t)

#map - used to apply the same function to every 
# item in the list and return the map object
l=[1,2,3,4,5]
def square(l):
    return l*l
nsquare=map(square,l)
print(list(nsquare))

#filter
l=[12,19,18,21,10,28]
def fill(x):
    if x>=18:
        return True
adult=filter(fill,l)
print(list(adult))

from functools import reduce

n=1,2,3,4,5,6
def red(a,b):
    return a*b
y=reduce(red,n)
print(y)


#duplicate element in the list
l=[1,2,3,4,3,2,4,6,7]
u=[]
d=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(d)

#occurnace of char
s="rushikeshR".lower()
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(str(op))

#2nd largets element in the list
l=[12,2,3,4,59,10]
l.sort()
print(l[-2])

#rearragne
d=str(78947689)
print("".join(sorted(d,reverse=True)))
print("".join(sorted(d,reverse=False)))

#prime of r not
n=7
if n<2:
    print("np")
else:
    for i in range(2,n):
        if n%i==0:
            print("np")
            break
    else:
        print("p")

#ovel and conso
# s=input("enter string: ").lower()
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


#genrator
def gen_s():
    for i in range(1,6):
        yield i*i
sq=gen_s()
for val in sq:
    print(val)

# break continue & pass
 
for i in range(10):
    if i==2:
        continue
    elif i==8:
        break
    elif i==1:
        pass
print(i)


# exception handling 
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print(" the code under finally is always execute")

# inheritance
# single
class Parent:
    def fun1(self):
        print("fun in parent")
class Child(Parent):
    def fun2(self):
        print("fun in child")
obj=Child()
obj.fun1()
obj.fun2()

# multiple inheritance
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

