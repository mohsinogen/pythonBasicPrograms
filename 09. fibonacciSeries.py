# Program to display the Fibonacci sequence up to n-th term

givenRange = int(input("Enter the Range:"))

num1, num2 = 0, 1
count = 0

if (givenRange <= 0):
   print("Please enter a positive integer")
elif (range == 1):
   print("Fibonacci sequence upto",nterms,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while count < givenRange:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1