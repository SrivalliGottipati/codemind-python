n=int(input())
for i in range(1,n+1):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
    c.sort()
    for i in c:
        if i!=max(c):
            print(i,end=" ")
    print(max(c))