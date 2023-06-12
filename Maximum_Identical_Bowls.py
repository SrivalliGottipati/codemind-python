def max_id(n,arr,s):
    for i in range(n,0,-1):
        if(s%i==0):
            return i
    else:
        return 0
n=int(input())
arr=map(int,input().split())
s=sum(arr)
l=max_id(n,arr,s)
print(l)