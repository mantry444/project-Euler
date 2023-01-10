#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
for i in range (1,501):
    for j in range (1,501):
        for k in range (1,501):
            x= pow (i,2)
            y= pow (j,2)
            z= pow (k,2)
            t= i * j * k
            t2=i + j + k 
            l3 = [i, j, k]
            if x + y == z and t2 ==1000 :
                print(t)
                print (l3)
              
               
        
                            
    
