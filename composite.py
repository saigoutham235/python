k=int(input())
factor=0
for i in range(1,k):
  if k%i==0:
    factor=i
if factor>1:
  print('yes')
elif n==1:
  print('invalid')
else:
  print('no')
