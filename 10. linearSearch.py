# a program to demonstrate linear search on a list

# making a list from user input
items = []
listLength = int(input("Enter the length of the List:"))
for j in range(0, listLength):
    print("Enter the element", j+1)
    element = int(input())
    items.append(element)
print(items)

#creating a function for linear search
elementToSearch = int(input("Enter the element to be Searched:"))
def linearSearch(alist, value):
    for i in range(len(items)):
        if items[i] == elementToSearch:
            return i
    return -1

#displaying the result
result = linearSearch(items, elementToSearch)
if result == (- 1):
    print("Item not found")
else:
    print("Item found at position {}".format(result))