#REVERSE:
n=123455
print(str(n)[::-1])
print("rushiiiiiiiiiiiiii")
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

s="rushikeshtole"
print(s[::-1])
def rstr(s):
    r=""
    for i in s:
        r=i+r
    return r
print(rstr(s))


#missing number in the list
l=[1,2,3,5,6,9,10]
miss=[]
for i in range(l[0],l[-1]):
    if i not in l:
        miss.append(i)
print(miss)

#nesteed to single
lst=[1,2,3,[4,5,6],[6,7,8]]
op=[]
for i in  lst:
    if isinstance(i,list):
        op.extend(i)
    else:
        op.append(i)
print(op)


#sep string n intere
l=["rushi",23,"golu",234,"tre",7,9]
s=[]
n=[]
for i in l:
    if type(i)==str:
        s.append(i)
    else:
        n.append(i)
print(s,n)

#occuirance of char

s="rushikeshr"
op={}
for i in s:
    if i in op:
        op[i]+=1

    else:
        op[i]=1
print(str(op))


m=[1,2,2,3,4,5,6,4,7,8,5]
d=[]
un=[]
for i in m:
    if i not in un:
        un.append(i)
    else:
        d.append(i)
print(d)
