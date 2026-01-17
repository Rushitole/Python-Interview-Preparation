#occurancae of char in the string 
s="rushikesh".lower()
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(op)
#seprate sting & interger
l=["r","d","s",3,4,5,6]
s=[]
n=[]
for i in l:
    if type(i)==str:
        s.append(i)
    else:
        n.append(i)
print(s,n)

# mising number in the list
l=[1,2,4,5,7,8,10]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#genrator( 
def gen_s():
    for i in range(1,6):
        yield i*i
sqaure=gen_s()
for val in sqaure:
    print(val)

#exception handling 
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("this block n=in always exucute")

#break,continue and pass
for i in range(6):
    if i==2:
        continue
    elif i==6:
        break
    elif i==1:
        pass
print(i)
 
#single inheritance  a>>b
class Parent:
    def func1(self):
        print("func in parent")
class Child(Parent):
    def func2(self):
        print("func in child")
obj=Child()
obj.func1()
obj.func2()

#map
l=[1,2,3,4,5]
def square(l):
    return l*l
sq=map(square,l)
print(list(sq))

#filter 
l=[12,13,18,19,20,27,26]
def fill(l):
    if l>=18:
        return True
adult=filter(fill,l)
print(list(adult))

# reduce
from functools import reduce
l=[1,2,3,4,5]
def red(a,b):
    return a*b
x=reduce(red,l)
print(x)

#rarrange digit
d=str(7189021398)
print("".join(sorted (d, reverse=True)))

# add to list
a=[1,2,3,4,5]
b=[6,7,8,9,10]
s=[(x+y) for (x,y) in zip(a,b)]
print(s)

#oveel and consonenet
s="rushikesh".lower()
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

#duplicate elemet in the list
l=[1,2,3,4,5,2,3,4,5,6,7]
d=[]
u=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(d,u)

#prime or not 
n=7
if n<2:
    print("np")
else:
    for i in range(2,n):
        if n%i==0:
            print("np")
            break
    else:
        print("prime")

#fabo
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fib(6))
""""""
