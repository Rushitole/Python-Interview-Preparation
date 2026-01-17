# missing number in the list

l=[1,2,3,5,7,10]
miss=[]
for i in range(l[0],l[-1]):
    if i not in  l:
        miss.append(i)
print(miss)


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

#rev string 
s="Rushabh"
print(s[::-1])
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))


n=783728399
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

#nested list into

l=[1,2,3,[4,5,6],[7,8]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#cmn element in the list
l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]
cmn=list(set(l1) & set(list(l2)))
print(cmn)


#combine 2 list to 1
a=[1,2,3,4,5]
b=[5,6,7,8,9]
s=[(x+y) for (x,y) in zip(a,b)]
t=[(x*y) for (x,y) in zip(a,b)]
print(s,t)

#fact
def fact(n):
    if n==1:
        return True
    else:
        return n*fact(n-1)
print(fact(5))

#fibo series
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fib(10))

#map --square
l=[1,2,3,4]
def square(l):
    return l*l
sq=map(square,l)
print(list(sq))

# filter --adults
l=[12,19,20,23,27,17,18]
def fill(x):
    if x>=18:
        return True
adult=filter(fill,l)
print(list(adult))

#reduce
from functools import reduce
n=[1,2,3,4,5]
def red(a,b):
    return a*b
y=reduce(red,n)
print(y)

# duplicates elements in the list
l=[1,2,3,4,5,6,4,3,2,9]
u=[]
d=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(d)

#occurnace of char
s="Rushikeshtoler".lower()
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(str(op))


#2nd largest
l=[12,29,26,89,78,28]
l.sort()
print(l[-2])


#raggarnge
d=str(760128762)
print("".join(sorted(d,reverse=True)))

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
        print("p")

    
#genrator
def gen_s():
    for i in range(1,6):
        yield i*i
sq=gen_s()
for val in sq:
    print(val)

#break continue pass
for i in range(10):
    if i==2:
        continue
    elif i==8:
        break
    elif i==1:
        pass
    print(i)

    #exeption handeling 
    try:
        k=5//0
        print(k)
    except ZeroDivisionError :
        print("ZeroDivisionError")
    finally:
        print( " code under finally is always execute")



# single in heritance
class Parent():
    def fun1(self):
        print("func in parent")
class Child(Parent):
    def fun2(self):
        print("fun in child")
obj=Child()
obj.fun1()
obj.fun2()

# multipleas inheritancee
class Father():
    def father(self):
        print(self.fathername)
class Mother:
    def mother(self):
        print(self.mothername)
class Son(Father,Mother):
    def parenr(self):
        print(self.fathername)
        print(self.mothername)
obj=Son()
obj.fathername="gajanan"
obj.mothername="sangita"
obj.parenr()


#vowel and conso
s="rushikesjh".lower()
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


#seprarate sting n int from the list
l=[1,2,"rushi","raju",7,"ram",10]
s=[]
n=[]
for i in range(0,len(l)):
    if  str(l[i]).isdigit():
        n.append(l[i])

    else:
        s.append(l[i])
print(n,s)


#sum fo n natural number
n=6
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


#pallindorm
s="nayan"
if s==s[::-1]:
    print("pallindrome")
else:
    print("not palindrome")

             
             