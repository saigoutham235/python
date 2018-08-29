a=int(input())
i =1
b= 0
c= 1
while(i<a+1):
           if(i <= 1):
                      result = i
           else:
                      result = b +c
                      b = c
                      c = result
           if(i<a):
           	k=' '
           else:
           	k=''
           print(result,end=k)
           i = i + 1
