n=int(input())
b=[int(x) for x in input().split()]
b.sort()
for i in range(0,n):
	if(i<n-1):
		k=' '
	else:
		k=''
	print(b[i],end=" " )
