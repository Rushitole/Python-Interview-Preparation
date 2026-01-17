#reverse string n int
n=21344324
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

#string
s="Akshay"
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

# fibo
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fib(8))

# decorator
def deco(func):
    def inner():
        print("I'm deco")
        func()
    return inner
@deco
def ordinary():
    print("i'm ordinary")
ordinary()

#comman element in the list
l=[1,2,3,4]
l2=[3,4,5,6]
cmn=list(set(l)&set(list(l2)))
print(cmn)

#nested to single
l=[1,2,3,[4,5,6],[7,8,9]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)
