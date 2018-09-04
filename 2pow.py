n=int(input())
for i in range(0,n):
    if(2**i==n):
        k="yes"
        break
    if(2**i >n):
        break
    else:
        k="no"
print(k)
