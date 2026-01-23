"""
Reverse string

Palindrome

Count vowels

Fibonacci

Factorial

"""

s="rushikesh"
print(s[::-1])

i=12345
print(str(i)[::-1])

#pallindrome
t="Nayan"
if t.lower()==t.lower()[::-1]:
    print("p")
else:
    print("np")

#count vovel
m="RushikesheE"
vovel="aeiouAEIOU"
count=0
for i in m:
    if i in vovel:
        count+=1

print(count)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fibo



