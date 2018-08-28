d=input()
c=0
for i in range(0,len(d)):
  if(d[i]!='.'):
	  if(d[i].isalnum()==False):
		  c+=1
print(c)
