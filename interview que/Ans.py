# 1.revrse string and int using slice and without slice

# 2.factorial of number

# 3.fibo series

# 4.decoarator with example

# 5.find comman element in the list

# 6.convert nested list to single list

# 7.map, filter and reduce with example

# 8.combine 2 list to one list

# 9.addition and multiplication of 2 list

# 10.print duplicate elemet in the list

# 11.print unique element in the list

# 12.Print even and odd element in the list

# 13.Occurnace of char in the string 

# 14.check weather number is prime or not

# 15.Rearrange digit from small to big

# 16.Rearrange digit from big to small

# 17.print owel and consonant from the string

# 18.Calculate the len of each string from list

# 19.print 1 to 100 in python

# 20.check weather pallindrome or not

# 21.polymorphisam with example

# 22.find the maximum product of 2 distinct element

# 23.print Fibo series 

# 24.Find missing number in the list.

# 25.separte string & number from the list.

# 26.Count the number of uppercase char in the list.


#reverse int
i=83989834
print(str(i)[::-1])
rev=0
while i>0:
    digit=i%10
    rev=rev*10+digit
    i//=10
print(rev)

#rev string
s="madhukar"
print(s[::-1])

def rstr(s):
    re=""
    for i in s:
        re=i+re
    return re
print(rstr(s))

# fact of number
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
(fibo(10))

#2nd largest element in the list
def deco(fuc):
    def inner():
        print("drco")
        fuc()
    return inner
@deco
def ordinary():
    print("i'mordiary")
ordinary()

#comman element in the list
l=[1,2,3,4]
l2=[3,4,5,6]
cm=list(set(l) & set(list(l2)))
print(cm)

#odd even
def is_even(n):
    return n%2==0
print(is_even(5))
print(is_even(6))

#max product of 2 distinct elemenet
l=[10,9,8,7,6]
def max(l):
    l.sort()
    return l[-1]*l[-2]
print(max(l))

#multi dic to 1
lst=[1,2,3,[4,5]]
op=[]
for i in lst:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)


#rev
s="hrehkhk"
def rs(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rs(s))


