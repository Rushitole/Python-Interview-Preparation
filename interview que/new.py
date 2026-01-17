#reverse
n=1234
print(str(n)[::-1])
s="ridsehk"
print(s[::-1])

N=12345
rev=0
while N>0:
    digit=N%10
    rev=rev*10+digit
    N//=10
print(rev)

#fact of number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fibo series
def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fibo(9)  )  

#2nd largest element in the list
l=[2,3,4,5,6]
l.sort()
print(l[-2])

#decorator
def deco(func):
    def inner():
        func()
        print("decorated")
    return inner
@deco
def ordinary():
    print("im ordinary")

ordinary()

#single in heritance
class Parent:
    def fun1(self):
        print("p func")
class Child(Parent):
    def fun2(self):
        print("c func")
obj=Child()
obj.fun1()
obj.fun2()

# max product of 2 distinct element
l=[10,20,30,40]
def maxp(l):
    l.sort()
    return l[-1]*l[-2]
print(maxp(l))

l2=[10,20,30,40]
l2.sort()
print(l2[-1]*l2[-2])

#print 1 to 100
for i in range(101):
    print(i)

#2 list to 1 list
l=[[1,2],[3,4,5,6],[7,8,9]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)

    else:
        op.append(i)
print(op)

#combine 2 list to 1
a=[1,2,3]
b=[4,5,6]
l=[(x+y) for (x,y) in zip(a,b)]
print(l)

#print duplicate elemet in the list
n=[2,3,4,5,6,2,3,4]
un=[]
dp=[]
for i in n:
    if i not in un:
        un.append(i)
    else:
        dp.append(i)
print(dp)

S="rudshikesh"
op={}
for i in s:
    if i in op:
        op[i]+=1
    else:
        op[i]=1
print(str(op))

