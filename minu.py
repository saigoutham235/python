a=int(input(" "))
h=0
b=a
for i in range(0,a+1):
	if(i%60==0 and i>=60):
		h+=1
		b-=60
print(h,b)
