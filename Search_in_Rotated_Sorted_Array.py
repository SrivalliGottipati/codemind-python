n=int(input())
a=list(map(int,input().split()))
y=int(input())
x=0
for i in range(n):
    if y==a[i]:
        print(i)
        x=1
        break
if x==0:
    print("-1")