# a program to demonstrate bubble sort for sorting a list of int

#making a list from user input
items = []
listlength = int(input("Enter the length of the unsorted list:"))
for i in range(0,listlength):
     print("Enter the element {} of unsorted list:".format(i+1))
     element = int(input())
     items.append(element)
print("The unsorted list is:", items)

# creating a function for bubble sort
def bubbleSort(items):
    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                
# calling the function and displaying the sorted list
bubbleSort(items)
print("The sorted list is:", items)