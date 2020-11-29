n= int(input())
wheretoswap = 0
a=[]
mini = 0
flag = 1
for i in range(n):
    x = int(input())
    a.append(x)
    if(x>0) and (flag==1):
        wheretoswap = i
        flag = 0
        continue
print(a)#Printing list before moveing operation done
for i in range(n):
    if(a[i]<0) and (i>wheretoswap):
        mini = i
        while(mini>wheretoswap):
            a[mini],a[mini-1] = a[mini-1],a[mini]
            mini-=1
        wheretoswap+=1
    else:
        continue

print(a)#Printing list after moveing operation done
