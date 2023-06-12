a,b=map(int,input().split())
if (a>0 and b>0):
    if(abs(a-b)==1 or a==1 and b==10 or b==1 or a==10):
        print("Yes")
    else:
        print("No")