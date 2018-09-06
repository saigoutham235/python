b=int(input())
g=0
for i in range(2,b//2+1):
    if(b%i==0):
        g=g+1
if(g<=0):
    print("yes",end="")
else:
    print("no",end="")
