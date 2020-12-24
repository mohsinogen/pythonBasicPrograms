# a program to demonstrate binary search on a sorted list

#making a list from user input

items=[]
listlength = int(input("Enter the length of the sorted list:"))
for i in range(0,listlength):
     print("Enter the element {} of sorted list:".format(i+1))
     element = int(input())
     items.append(element)
print(items)

# creating a function for binary search

elementToSearch = int(input("Enter the element to be searched:"))
def binarySearch(items,elementToSearch):
     first = 0
     last = len(items)-1
     while(first<=last):
          mid = int((first+last)/2)

          if items[mid] == elementToSearch:
               return mid
          else:
               if elementToSearch<items[mid]:
                    last = mid-1
               else:
                    first = mid+1
     return -1

#displaying the result
result = binarySearch(items, elementToSearch)
if result == (- 1):
    print("Item not found")
else:
    print("Item found at position {}".format(result))
