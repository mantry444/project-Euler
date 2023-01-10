#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#import numpy as np
x= int(999/3)
#sum = {3 * x*(x-1)}/2
X=3*x*(x+1)/2
y = int(999/5)
Y=5*y*(y+1)/2
z= int(999/15)
Z=15*z*(z+1)/2
S=X+Y-Z
print(S)
 
