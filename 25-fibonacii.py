a=1



import math
a= 1
b= 2
c=0
s=[]
while  c < (10**999) :
    c = a+b
    a=b 
    b=c
    s.append(c)
x=len(s)
print(x+3)   # the frst number is 3 which is is the 3rd position. So used x+3 
