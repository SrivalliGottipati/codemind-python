r,c=map(int,input().split())
mat=[]
for i in range(r):
    sub_list=sum(list(map(int,input().split())))
    mat.append(sub_list)
    y=sum(mat)
print(y)