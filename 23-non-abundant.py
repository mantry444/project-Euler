from sympy import divisors
import time
t1=time.time()
m=[]
for i in range(1,28124):
    l=list(divisors(i))
    l.pop(-1)
    z=sum(l)
    if z > i:
        m.append(i)
#print(m)  # All the numbers who are abundant numbers  
f=[]
for j in m :
    for k in m:
        t=k+j
        f.append(t)
#print(f)        
A=set(f) # all the numbers which are sum of (abundant numbers within range 12823)
M=[]
for s in A :
    if  s < 28124:
        M.append(s) # All the numbers after sum, the resultant is within 12823
SUM=sum(M)  #sum of numbers who are written as sum of 2 abudant number 

val=int((28123*28124)/2)
Ans=val-SUM
print(str(Ans) +" is the answer")      # This is the answer
t2=time.time()
print("time taken is " + str(t2-t1)+"s")