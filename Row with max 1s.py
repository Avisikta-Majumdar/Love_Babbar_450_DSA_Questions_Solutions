def rowWithMax1s(self,arr, n, m):
	    s=0
	    res=-1
		for i in range(n):
		    if sum(arr[i])>s:
		        res,s=i,sum(arr[i])
		return res
