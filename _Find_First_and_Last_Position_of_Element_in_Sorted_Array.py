n=int(input())
a=list(map(int,input().split()))
a.sort()
y=int(input())
x=0
for i in range(0,n):
    if y==a[i]:
        print(i,end=" ")
        x=1
        break
for i in range(n-1,-1,-1):
    if y==a[i]:
        print(i,end=" ")
        x=1
        break
if x==0:
    print("-1 -1")