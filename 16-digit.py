#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^(1000)?

n=pow(2,1000)
n1=str(n)
n2=map(int,n1)
l=(list(n2))
print(sum((l)))
