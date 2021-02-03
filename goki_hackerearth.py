l=[]
number_of_elements=int(input())
Condition=int(input())
for i in range(number_of_elements):
    a=int(input())
    l.append(a)
print(l)
for i in l:
    if(i >= Condition):
        print("ÿes")
    else:
        print("no")
