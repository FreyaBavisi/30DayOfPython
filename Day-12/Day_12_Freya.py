n=int(input("enter size of array"))
a=[]
j=0
flag=0
for i in range(0,n):
    x=int(input("enter element"))
    a.append(x)
print(a)
y=int(input("enter element you want to search"))
for j in range(len(a)):
    if(a[j]==y):
        print(j)
        flag=1
if flag==0:
    print(-1)
