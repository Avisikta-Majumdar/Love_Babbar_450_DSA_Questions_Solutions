class Solutions:
    def rotate(self , a,r,n):
        i=(n-1)
        temp =1
        while(temp==1):
            for j in range(n):
                print(a[i][j],end=' ')
            print()
            i-=1
            if i==(-1):
                temp=0

        return 1



Object = Solutions()
r ,c =(int(input()) for i in range(2))
a=[]
for j in range(r):
    x=[]
    for k in range(c):
        x.append(int(input()))
    a.append(x)
print(a)
       
       
ans = Object.rotate(a, 3,3)
print(ans)
