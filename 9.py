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
              
               
        
                            
    