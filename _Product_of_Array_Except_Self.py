n=input()
a=list(map(int,input().split()))
for i in a:
    c=1
    for j in a:
        if i!=j:
            c=c*j
    print(c,end=" ")