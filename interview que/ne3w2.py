#revrse string wihthout slice

def rstring(s):
    rev=''
    for i in s:
        rev=i+rev
    return rev
print(rstring("rushi"))

#rev int without slice
n=12345
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

s="niki"
print(s[::-1])
n=1234
print(str(n)[::-1])

#find cmn element in the list
l=[12,21,23,12,12,11,15,89,70,30]
dup=[]
un=[]
for i in l:
    if i not in un:
        un.append(i)
    else:
        dup.append(i)
print(dup,un)

#prime or not
n=9
if n<2:
    print("np")
else:
    for i in range(2,n):
        if n%i==0:
            print("np")
            break
    else:
        print("p")

#occurance of element in the list
l="rushikesh"
ele={}
for i in l:
    if i in ele:
        ele[i]+=1
    else:
        ele[i]=1
print(ele)

#missing number in the list
l=[1,2,3,4,5,10]
m=[]
for i in range(l[0],l[-1]):
    if i not in l:
        m.append(i)
print(m)

#nested list to single list
l=[[1,2,3],[7,8,9]]
op=[]
for i in l:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)

#count number of uppercase
def cnt(n):
    return sum(1 for i in n if i.isupper())
print(cnt("RusYhiT"))

#print even number in the list
l=[1,2,3,4,5,6,7,8]
for i in l:
    if i%2==0:
        print(i)

#Map,filter and reduce
l=["rushi","golu","sangita","ragini"]
def myfuc(n):
    return len(n)
x=map(myfuc,l)
print(list(x))

ages=[12,17,18,19,21,22,39]
def fill(n):
    if n>=18:
        return True
a=filter(fill,ages)
print(list(a))

from functools import reduce
l=[2,3,4,5]
def red(a,b):
    return a*b
v=reduce(red,l)
print(v)






