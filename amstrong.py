n=int(input(""))
sum=0
t=n
while(n>0):
	rem=n%10
	sum+=rem**3
	n=n//10
if(sum==t):
	print("yes",end="")
	
else:
	print("no",end="")
