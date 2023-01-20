#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names
# , begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
#  multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?


#   Answer starts from here
m=[]
p=list(open("/home/rk/ML/euler/22.txt").read().replace('"','').split(',')) # read the txt file and remove "" to make it in a list 
p.sort() # sort the number 

for i in p:
    x=[*i] # to make 'abc' as 'a','b','c'
    m.append(x)
aa=[] 
for j in range(0,len(m)) :
    n=[] 
    mm=[]
    for k in m[j]:
        y=ord(k)-64 # as A has number 65
        mm.append(y)
        d=y*(j+1) # j+1 because index start from 0 but position is start from 1
        n.append(d) 
    #print(n)
    Q=(sum(n)) # q is the indivisual sum of each name
    #print(Q)
    #print(mm)   
    aa.append(Q)
print(sum(aa))  
print(p[937])   
print("So the answer is "+ str(sum(aa))) 