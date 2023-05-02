t=int(input())
for i in range(t):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    s=len(a)
    for j in range(0,s):
        if a[j]%2!=0:
            c+=1
    print(c//2)