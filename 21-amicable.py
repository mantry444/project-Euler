#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.





from sympy import divisors
m=[]
q=[]
for i in range(1,10001):
    l=list(divisors(i))
    l.pop(-1)          # exclude the 'n' number from the list of divisors of n.so it can be a list of proper divisors
    #print(i,l)
    a=sum(l)          # sum of proper divisors 
    e=(i,a)
#print(i,a)

    m.append(e)       # m gives the list of pair where 1st number is the number and 2nd number is the sum of proper divisors 
#print(m)   
for s,d in m:          #This loop will help to consider each one of first no. with all 2nd numbers of the pair 
    for s1,d1 in m :
        if s==d1 and d==s1 and s!=d:   #This is to check that 2nd number of 1st pair= 1st number of 2nd pair and vice versa
            print(s)                    # and a!=b
            q.append(s)
print("the ans is : "+ str(sum(q)))