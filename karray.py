n,k=map(int,raw_input().split())
n=list(map(int,raw_input().split()))
sum=0
for i in range(0,(k+1)):
	sum=sum+i
	n.append(sum)
print(sum)
