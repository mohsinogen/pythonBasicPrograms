# a program to demonstrate insertion sort for sorting list of int

#making a list from user input
items = []
listlength = int(input("Enter the length of the unsorted list:"))
for i in range(0,listlength):
     print("Enter the element {} of unsorted list:".format(i+1))
     element = int(input())
     items.append(element)
print("The unsorted list is:", items)

# creating a function for insertion sort
def insertionSort(items):
     for i in range(1, len(items)):
          temp = items[i]
          j = i - 1
          while j >= 0 and temp < items[j]:
               items[j + 1] = items[j]
               j -= 1
               items[j + 1] = temp

# calling the function and displaying the result
insertionSort(items)
print("The sorted list is:", items)

