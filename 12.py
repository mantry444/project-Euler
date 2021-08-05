import os
import math
duration = 3  # seconds
freq = 400
t=[]
t2=[]
t1=[]

def factors(num):
    l=[]
    a1=math.floor(math.sqrt(num)+1)
    for j1 in range (1,a1):
      if num % j1 == 0:
        l.append(j1)
    return (len(l))        
 # z= int(num2)+1
for i in range (1000999):
     #,2050):
    tn=int(((i+1)*i)/2)
    t.append(tn)
    for s in t:
        if factors(s) > 250:
            print(s)
            break
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))             

# took a long time . Try another method.