a=int(input())
i = 0
b= 0
c= 1
while(i<a):
           if(i <= 1):
                      result = i
           else:
                      result = b +c
                      b = c
                      c = result
           if(i<a-1):
           	k=' '
           else:
           	k=''
           print(result,end=k)
           i = i + 1
