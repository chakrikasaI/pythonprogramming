r=int(input())
l=[]
for n in range(1,6):
  k=n*r
  l.append(k)
for m in range(0,len(l)):
  if(m==len(l)-1):
    print(l[m],end="")
  else:
    print(l[m],end=" ") 
