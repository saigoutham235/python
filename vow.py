ch=list(input())
for i in ch:
  if((i>'a' and i<'z') or (i>'A' and i<'Z')):
    print("yes")
    break
  else:
    print("no")
    break
