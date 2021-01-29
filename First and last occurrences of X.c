#include <stdio.h>
int main() {
	int testcase ;
	scanf("%d",&testcase);
	while(testcase--)
	{
	    int n,x;scanf("%d %d",&n,&x);int arr[n];
	    for(int i=0;i<n;++i)
	    scanf("%d",&arr[i]);
	    int start=-1,end=0;
	    for(int i=0;i<n;++i)
	    {
	        if((x==arr[i])&&(start==-1))
	        {
	            start=i;
	            end=i;
	        }
	        else if(x==arr[i])
	        {
	            end=i;
	        }
	        else
	        {
	            continue;

	        }
	    }
	    (start>=0)?printf("%d %d\n",start,end):printf("-1\n");
	}
}
