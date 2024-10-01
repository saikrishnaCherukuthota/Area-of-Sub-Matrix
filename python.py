m,n=map(int,input().split())
l=[]
for j in range(m):
    l1=list(map(int,input().split()))
    l.append(l1)
k=int(input())
p=[]
for i in range(m):
    for j in range(n):
        if i>=k and j>=k and i<m-k and j<n-k:
            p.append(l[i][j])
if len(p)>0:
    j=1 
    for k in p:
        j=j*k
    print(j)
else:print(0)
