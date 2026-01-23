# 1.revrse string and int using slice and without slice

# 2.factorial of number

# 3.fibo series

# 4.decoarator with example

# 5.find comman element in the list


s="Rishikesh"
print(s[::-1])

#count vovel in string

s1="Rushieksh" 
count=0
for i in s1:
    if i in "aeiou":
        count=count+1
print(count)

#find dupliocates elements in the list
l=[1,2,3,4,4,5,3,6,7]
d=[]
u=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(d)
print(u)

text="Python support all datatype"
words=text.split()
freq={}
for i in words:
    freq[i]=freq.get(i,0)+1
print(freq)



