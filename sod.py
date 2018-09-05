m=int(input())
t=0
while(m>0):
    dig=m%10
    t=t+dig
    m=m//10
print(t)
