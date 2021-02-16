from itertools import combinations 

s=input("Enter any string:-")
s=[i for i in s]
length = len(s)
for j in range(1,length+1):
    comb = combinations(s, j) 
    # Print the obtained combinations 
    for i in list(comb): 
           # print (i)
            separator =''
            a= separator.join(i)
            #print(a,end=' , ')
            print(a,end=', ') if j!=length else print(a)
