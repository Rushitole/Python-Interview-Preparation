#revewrse Int both way

n=8765321
print(str(n)[::-1])
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

# rev string 
s="rushikesh"
print(s[::-1])
def rstr(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
print(rstr(s))

#Factorial of number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))