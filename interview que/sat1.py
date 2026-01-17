#revese string
s="rushikesh"
print(s[::-1])
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))

#rvsrse interger
n=987655441
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)        
#n%10 --> get last digits
#rev*10+digit append digit at the end of rev
#n//=10 remove last digit from num


#fact
def fact(n):
    if n==1:
        return 1

    else:
        return n*fact(n-1) 
print(fact(5))

#fibboo series
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fib(5))


#decorator
def deco(func):
    def inner():
        print("i'm deco")
        func()
    return inner
@deco
def ordinary():
    print("i'm ordinary")
ordinary()


#comman elemenyt ih the list
l1=[1,2,4,5]
l2=[4,5,6,7]
cmn=list(set(l1)& set(list(l2)))
print(cmn)

#missing element in the list
l=[1,2,3,5,7,10]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#sprate sting and inetger
l=["r",2,3,4,"t","you"]
s=[]
d=[]
for i in l:
    if type(i)==str:
        s.append(i)
    else:
        d.append(i)
print(s,d)

#nested list to single list
l=[1,2,3,[5,6,7],[3,5]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#map 
l=[1,2,3,4,5]
def square_s(l):
    return l*l
sq=map(square_s,l)
print(list(sq))

#filter
l=[12,18,16,17,20,23]
def fill(x):
    if x>=18:
        return True
adult=filter(fill,l)
print(list(adult))

#ereduce
from functools import reduce
l=[1,2,3,4]
def red(a,b):
    return a*b
v=reduce(red,l)
print(v)

#duplicate element in the list
l=[1,3,4,3,5,7,8,9,5]
d=[]
u=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(u,d)

#occurance of char in the string
s="rushikesh".lower()
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(op)

#rearrange digit 
d=str(98737080890)
print("".join(sorted(d,reverse=True)))

#2nd largest elemet in the list
l=[12,34,5,6,72,4]
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
        print("p")

#ovel and consonent
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
print(c,v)


#max producnt of 2 distinc elemeent
l=[1,23,15,10,17]
l.sort()
print(l[-1]*l[-2])

#odd even
n=7
if n%2==0:
    print("even")
else:
    print("odd")

#genrator
def gen_s():
    for i in range(1,6):
        yield i*i
square=gen_s()
for val in square:
    print(val)

#break continue pass
for i in range(6):
    if i==2:
        continue
    elif i==6:
        break
    elif i==2:
        pass
print(i)

#exeption handling 
try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("always execute")

#pallindrome
s="nayan"
if s==s[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")


