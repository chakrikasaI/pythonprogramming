r,k=map(int,input().split())
l=[]
for n in range(r+1,k):
  m=n
  u=0
  while m>0 :
    d= m % 10
    u += d ** 3
    m//=10
  if n == u :
    l.append(n)
for p in range(0,len(l)):
  if(p == len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end=" ") 
