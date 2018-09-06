b,g=map(int,raw_input().split())
b=list(map(int,raw_input().split()))
s=0
for i in range(0,(g+1)):
	s=s+i
	b.append(s)
print(s)
