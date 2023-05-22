n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range (len(a)):
    for j in range(1,a[i]+1):
        if(a[i]==j*j):
            sum+=a[i]
print(sum)