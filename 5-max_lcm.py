#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



import numpy as np
l=[]
m=[]
for i in range (11,21,2):
    a=np.lcm(i,i+1)
    l.append(a)
#print(l) 
for j in range(1,5,2):
    b=np.lcm(l[j],l[j+1])
    #print(l[j])
    #print(b)
    m.append(b)
#print(m)
print(np.lcm((np.lcm(m[0],m[1])),l[0]))
#print(l[0])
