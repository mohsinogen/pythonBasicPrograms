# a program to demonstrate selection sort for sorting list of int

#making a list from user input
items = []
listlength = int(input("Enter the length of the unsorted list:"))
for i in range(0,listlength):
     print("Enter the element {} of unsorted list:".format(i+1))
     element = int(input())
     items.append(element)
print("The unsorted list is:", items)

#creating a function for selection sort
def selectionSort(items):
    for i in range(len(items) - 1, 0, -1):
        pos = 0
        for j in range(1, i + 1):
            if items[j] > items[pos]:
                pos = j

        items[i], items[pos]= items[pos], items[i]


selectionSort(items)
print("The sorted list is:", items)