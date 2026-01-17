#reverse srting & int both way
s="rushikesh"
print(s[::-1])

def revs(s):   
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(revs("Gaurav"))

n=123456
print(str(n)[::-1])

n=123456
nrev=0
while n>0:
    digit=n%10
    nrev=nrev*10+digit
    n//=10
print(nrev)

#pallindrome
def pall(n):
    return n==n[::-1]
    
print(pall("nayan"))

#fact
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

#cnt uppercase char
def count(n):
    return sum(1 for char in n if char.isupper())
print(count("rushT"))


#single inheritance
class Parent:
    def fun1(self):
        print("fun in p")

class Child(Parent):
    def fun2(self):
        print("fun in Child")

obj=Child()
obj.fun1()
obj.fun2()


#max product of 2 ditinct element
l=[10,2,3,4]
def max(l):
    l.sort()
    return l[-1]*l[-2]
print(max(l))
