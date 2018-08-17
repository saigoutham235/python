n=int(input(""))
temp=n
rev=0
#for i in range(0,n):
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
if(temp==rev):
    print("yes",end="")
else:
    print("no",end="")
