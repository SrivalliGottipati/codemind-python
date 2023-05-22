a,b,c=map(int,input().split())
a=list(map(int,input().split()))
o=[]
for i in range(c):
    o.append(int(input()))
for i in range(b):
    y=a[-1]
    a.remove(y)
    a=a[::-1]
    a.append(y)
    a=a[::-1]
for i in o:
    print(a[i])