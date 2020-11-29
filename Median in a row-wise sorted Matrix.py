class Solution:
    def median(self, matrix, r, c):
    	 a=[j for i in range(r) for j in matrix[i] ]
    	 a.sort()
    	 le=len(a)
    	 if len(a)&1 ==1:
    	     return a[(le//2)]
    	 else:
    	     mediaan = (a[(le//2)] + a[1+(le//2)])/2
    	     return mediaan
if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
