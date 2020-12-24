# program to calculate sum of even and odd number in given range

sumOfEven = 0
sumOfOdd = 0
i = 0
range = int(input("Enter the Range:"))

while (i <= range):
    if (i % 2 == 0):
        sumOfEven = sumOfEven + i
        i = i+1
    elif (i % 2 != 0):
        sumOfOdd = sumOfOdd + i
        i +=1

print("The sum of Even numbers is:", sumOfEven)
print("The sum of Odd numbers is:", sumOfOdd)