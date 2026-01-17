# rev INT
n=8319834
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

# rev string
s="rushikesh"
def sstr(s):
    rev=''
    for i in s:
        rev=i+rev
    return rev
print(sstr(s))

#deco
def deco(fun):
    def inner():
        print("deco")
        fun()
    return inner
@deco
def ordi():
    print("ord")
ordi()
    
# rev
s="gajanan"
def rev(s):
    re=""
    for i in s:
        re=i+re
    return re
print(rev(s))

#cmn element in ythe lisy
l=[1,2,3,4]
l2=[3,4,5,6]
cmn=list(set(l) & set(list(l2)))
print(cmn)

#nesteed tto single
l=[1,2,[3,4],[5,6]]







