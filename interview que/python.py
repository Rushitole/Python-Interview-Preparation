
#reverse number n int
n=r"rushi"
print(n[::-1])
i=12345
print(str(i)[::-1])

n=26743187
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)
# #rev int n string wo slice
# s="rushikesh"

# def rstr(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# print(rstr(s))

#palindrome or not
def pall(p):
    return p==p[::-1]
print(pall("nayan"))

#factorial 
def fact(n):
    if n==0:
        return 1
    else:
        return n *fact(n-1)
print(fact(5))

#fibo serires
def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
print(fibo(10))


#2nd largest element in the list
l=[12,10,23,29,34,6,78]
l.sort()
print(l[-2])

#decorator
def deco(func):
    def inner():
        print("im deco")
        func()
    return inner
@deco
def ordinary():
    print("im ordi")
ordinary()

#comman element in the list
l=[1,2,3,4]
l2=[3,4,5,6]
cmn=list(set(l) & set(list(l2)))
print(cmn)

#odd n even number
def is_even(n):
    return n%2==0
print(is_even(4))
print(is_even(5))

#find max product of 2 distinct element
l=[10,2,3,4,5]
def max(l):
    l.sort()
    return l[-1]*l[-2]
print(max(l))

#multi dict to 1
lst=[1,2,3,[4,5]]
op=[]
for i in lst:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

a=[1,2,3]
b=[4,5,6]
z=[(m+n) for(m,n) in zip(a,b)]
print(z)
print(a+b)




s="kdhfkkfdk"
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))