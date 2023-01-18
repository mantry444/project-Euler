#Starting in the top left corner of a 2×2 grid, and 
# only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?


from math import factorial
a=factorial(40)
b=factorial(20)
c=pow(b,2)
ans=a/c    #the answer is (m+n)^C_m ie combination nCr.
print(ans)
