r,k=map(int,input().split())
l=[]
for val in range(r+1,k):
  if val>1 :
    for k in range(2,val):
      if(val%k)==0:
        break
    else:
      l.append(val)
for m in range(0,len(l)):
  if(m==len(l)-1):
    print(l[m],end="")
  else:
    print(l[m],end=" ")  
