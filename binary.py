k=input()
count=0
for i in range(0,len(k)):
  if(k[i]=='0' or k[i]=='1'):
    count=count+1
if(count==len(k)):
  print("yes")
else:
  print("No")

