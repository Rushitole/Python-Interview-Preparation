# missing nunber in the list
l=[1,2,3,4,5,7,8,10]
miss=[]
for i in range(l[0],l[-1]):
        if i not in l:
            miss.append(i)
print(miss)

#seprate sting n integer
l=["r",3,"t","th",4,8]
s=[]
n=[]
for i in l:
    if type(i)==str:
        s.append(i)
    else:
         n.append(i)
print(s,n)

#vovel n conso
s="rushikeshtole".lower()
vowel="aeiou"
c=[]
v=[]
for i in s:
    if i.isalpha():
        if i in vowel:
            v.append(i)
        else:
            c.append(i)
print(c,v)

#nested list to 1
l=[1,2,[3,4],[5,6]]
op=[]
for i in l:
    if isinstance(i,list):
         op.extend(i)
    else:
         op.append(i)
print(op)
    
#occurnace of char 
s="rushikeshtole".lower()
op={}
for i in s:
     if i in op:
          op[i]+=1
     else:
          op[i]=1
print(op)

#fibo
def fibo(n):
     a,b=0,1
     for i in range(n):
          print(a)
          a,b=b,a+b
print(fibo(5))

#map
l=[1,2,3,4,6]
def map_s(l):
     return l*l
square=map(map_s,l)
print(list(square))

#filter
l=[12,181,19,15,10]
def fill(x):
     if x>=18:
          return True
adult=filter(fill,l)
print(list(adult))

# reduce
l=[1,2,3,4]
def red(a,b):
     return a*b
from functools import reduce
v=reduce(red,l)
print(v)

