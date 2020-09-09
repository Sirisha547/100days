n=int(input("enter a range"))#3
a=0
b=1
print(a,b,end=" ")#0,1
for i in range(2,n+1):#2,4
    c=a+b#1,2
    a=b#1,1
    b=c#1,2
    print(b,end=' ')#1,2
