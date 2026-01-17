# #rev int n string wo slice
# s="rushikesh"

# def rstr(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# print(rstr(s))

# n=6789
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)

# #factorial
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# #fibbo series

# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b

# print(fibo(9))

# #decoarator
# def deco(func):
#     def inner():
#         print("decorator func")
#         func()
#     return inner
# @deco
# def ordinary():
#     print("ordinary fucn")
# ordinary()

# s="Gajanan"
# def revs(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# print(revs(s))

# n=987654321
# r=0
# while n>0:
#     digit=n%10
#     r=r*10+digit
#     n//=10

# print(r)


# #cmn element in the list
# l=[1,2,3,4]
# l2=[3,4,5,6]
# cmn=list(set(l) & set(list(l2)))
# print(cmn)

# #nested to single list

# l=[1,2,3,[4,5,6],[7,8,9]]
# op=[]
# for i in l:
#     if isinstance(i,list):
#         op.extend(i)
#     else:
#         op.append(i)
# print(op)

# #Combine 2 list to 1 list
# a=[1,2,3,4]
# b=[5,6,7,8]
# z=[(x*y) for (x,y) in zip(a,b)]
# print(z)
# print(a+b)
# s=[x**2 for x in b]
# print(s)


# #print duplicate elemet in the list
# l=[1,2,3,4,4,5,3,2,7,8]
# d=[]
# un=[]
# for i in l:
#     if i not in un:
#         un.append(i)
#     else:
#         d.append(i)
# print(un,d)

# #even odd
# a=[1,2,3,4,5]
# o=[]
# e=[]

# for i in a:
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
            
# print(o,e)

# def is_evn(a):
#     return a%2==0
# print(is_evn(2))

# #occurnace of char

# s="SaRHsksoi"
# op={}
# for i in s :
#     if i in op:
#         op[i]+=1

#     else:
#          op[i]=1
  
# print(str(op))     

# t="rushikesh"
# p={}
# for i in t:
#     if i in p:
#         p[i]+1

#     else:
#         p[i]=1
# print(str(p))


# #map filter an d reduce
# l=["rushi","golu","nayan","kittuooo"]
# def mapp(n):
#     return len(n)
# x=map(mapp,l)
# print(list(x))

# #filter
# ad=[21,23,45,18,15,16,20,17]
# def fill(n):
#     if n >=18:
#         return True
# l=filter(fill,ad)
# print(list(l))

# #reduce
# from functools import reduce
# l=[2,3,4,5]
# def red(a,b):
#     return a*b
# v=reduce(red,l)
# print(v)

# #prime or not
# a=9
# if a<2:
#     print("np")
# else:

#     for i in range(2,a):
#         if a%i==0:
#             print("np")
#             break
#     else:
#         print("p")



#frequently user char
s="infosys"
fre={}
for i in s:
    fre[i]=fre.get(i,0)+1
print(fre)

# #rearrange digit from largest to small or vise versa
# n=str(768687897)
# print("".join(sorted(n,reverse=True)))

# # print ovel and consonent from the string
s=input("enter string  : ").lower()
vovel="aeiou"
vl=[]
cl=[]
for i in s:
    if i.isalpha():
        if i in vovel:
            vl.append(i)
        else:
            cl.append(i)
print("vowel :",vl)
print("consonant :",cl)









# revrerse int
i=821089
print(int(str(i)[:-1]))
