num = int(input("Enter a number: "))  
fact = 1  
if num < 0:  
   print("Sorry, fact does not exist for negative numbers")  
elif num == 0:  
   print("The fact of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       fact = fact*i  
   print("The fact of",num,"is",fact)  
