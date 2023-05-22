n=int(input())
c=0
b=[]
for i in range(1,n+1):
    a=int(input())
    b.append(a) 
x=int(input())
for i in b:
    if i<=x:
        c+=1
    else:
        c+=2
print(c)