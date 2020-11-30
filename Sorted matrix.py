testcase = int(input())
for i in range(testcase):
    size = int(input())
    array =input().strip().split()
    arr=[int(a) for a in array]
    arr.sort()
    for i in arr:
        print(i,end=' ')
    print()
