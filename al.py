s=input()
c1=0
c2=0
for i in s:
	if(i.isalpha()):
		c1+=1
	if(i.isnumeric()):
		c2+=1
		
if(c1>0 and c2>0):
	print('Yes')
else:
	print('No')
