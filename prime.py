k = int(input("Enter a number: "))  
  
if k > 1:  
   for i in range(2,k):  
       if (k % i) == 0:  
           print(k,"is not a prime number")  
           break  
   else:  
       print(k,"is a prime number")  
  
