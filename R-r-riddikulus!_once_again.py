x,b=map(int,input().split())
a=list(map(int,input().split()))
for i in range(b):
    x=a[0]
    a.remove(x)
    a.append(x)
print(*a)