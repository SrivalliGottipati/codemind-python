n=int(input())
su=0
for i in range(1,n):
    if(n%i==0):
        su=su+i
if(n==su):
    print(True)
else:
    print(False)