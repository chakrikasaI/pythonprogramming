fact=1
k=int(input())
if k<0:
  print("invalid")
elif k==0:
   print(" ",1)
else:
   for i in range(1,k+1):
     fact=fact*i
print(fact)
