ch=list(input())
count=0
for i in ch:
  if(i=='a' or i=='e' or i=='i' or i=='u' or i=='o' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
   count=count+1
   break
if(count==0):
  print("no")
else:
  print("yes")
