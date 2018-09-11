g=int(input())
c=''
while(g!=0):
	h=g%10
	if h%2!=0:
            c=c+' '+str(h)
	g=g//10
print(c[::-1])
