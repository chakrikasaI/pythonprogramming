n=int(input())
k=0
t=n
while t>0 :
  m=t%10
  k+=m**3
  t//=10
if n==k :
  print("yes")
else:
  print("no") 
