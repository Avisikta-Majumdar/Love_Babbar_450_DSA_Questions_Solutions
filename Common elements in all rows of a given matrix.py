class Solutions:
    def rotate(self , a,r,n):
        x = set(a[0])
        for i in range(1,r):
            b= set(a[i])
            x = x.intersection(b)    
        return x
Object = Solutions()
r ,c =(int(input()) for i in range(2))
a=[]
for j in range(r):
    x=[]
    for k in range(c):
        x.append(int(input()))
    a.append(x)   
ans = Object.rotate(a, r,c)
for i in ans:
    print(i,end =' ')
