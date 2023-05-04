n=int(input())
s=n*n
p=0
for i in str(s):
    p=p+int(i)
if(p==n):
    print("Neon Number")
else:
    print("Not Neon Number")