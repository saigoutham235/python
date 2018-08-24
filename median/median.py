n=int(input())
a=[int(x) for x in input().split()]
k=int((n+1)/2)
if(k%2==0):
	print(a[k-1],a[k])
else:
	print(a[k-1])

	
