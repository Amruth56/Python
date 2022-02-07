# list items are ordered, mutable and allows duplicate values.

from ast import comprehension
from numpy import append


myList = ["apple","babana","mango"]
print (myList)
print(type(myList))
print(len(myList))


thisList = list (('apple','qwerty','jshshf')) #It is possible to use list() constructor while creating a list.
print(thisList)

# Creating multidimensional list
List=[["apple","Banana"],["Mango"]]
print(List)



# Elements can be added to the list using append() function 
addList = []
print("initially its blank")
addList.append(1)
addList.append(2)
addList.append(3)
print("\nThe list after addition of 3 elements :")
print(addList)

# using loop
for i in range(4,11):
    addList.append(i)
print("\nList after addition of elements using for loop :")
print(addList)

# adding tuple to the list
addList.append((69,96))
print(f'\nadding tuple to the previous list {addList}\n') #similarly we ca add list to list ... 

# USING insert ( position,value )  method
# append() method is used to add element to the end but insert() method is used for the addition of elemenmmts to the list in desired position.

myList=[]
print("\nInitially empty")
myList.append(1)
myList.append(2)
myList.append(3)
print(f'myList after append of 3 numbers\t {myList}')
myList.insert(1,11)
myList.insert(3,22)
myList.insert(5,33)
print(f"myList after the insert of 3 elements at the desired position \t{myList}\n")


# USING extend() method
# This method is used to add multiple elements into the list at the same time 
List=[1,2,3,4]
print(f"\nInitial list {List}")
List.extend([77,66,44,"HEllo", "World"])
print(f"List after using extend function \t{List}")


                                        #ACCESSING ELEMENTS FROM THE LIST
X=["Accessing",'elements','from','the','list']
print(f'Accessing element from the List \t{X[0]} ,{X[3]}')
# Multidimensional list
A=[['indian','Institute',"of","Information","Technology"],["Dharwad","Karnataka"]]
print(f"Accessing elements from multidimensional array \t\t{A[0][4]} ,{A[1][0]} ,{A[1][1]}\n")
#Negative Indexing
Q=["H",'E','L','L','O']
print(Q[-1])


                                        #Removing elements from the list
#Using remove() function, it removes only 1 element at a time 
rem=[1,2,3,4,5,6,7,8,9,0]
print(f"Initial list\t {rem} ")
rem.remove(2)
rem.remove(3)
print(f"the list of numbers after using remove function are\t {rem}")
#removing elements from the list using iteration method
remov=[1,2,3,4,5,6,7,8,9,00]
for i in range(0,3):
    remov.remove(i)
print(f"removal of elements using iteration method\t {remov}\n")


                                        # Using pop() method
# by default it only removes the last element of the list, so to remove the specific elemet from the specific position, the index of the element is passed as an argument to the pop() method.

po=[11,22,33,44,55,66,77,88,99]
print(f"\nelements in the list are\t {po}")
print(f"popped element is \t {po.pop()}")
print(f"element in the list after poping last element\t {po}")
print(f"popped element is\t {po.pop(3)}")
print(f"element in the lis after poping an elememt from specific location\t {po}\n")


                                        # SLICING OF A LIST
# its performed with the help of a colon(:)
#  *** to print the whole list with slicing operation we use [:], to print the whole list in reverse order we use [::-1]

slic=[1,2,3,4,5,6,7,8,9,10]
print(f"\nInitial list =\t {slic}")
x=slic[2:7]
print(f"sliced list =\t {x}")
y=slic[3:]
print(f"To print the element from pre defined point to end =\t {y}")
z=slic[:]
print(f"To print the element from begining to end =\t {z}")
a=slic[::-1]
print(f"To print the element in reverse order =\t {a}")
g=slic[:-6]
print(f"To print the element from the begining to defined point through negative indexing =\t {g}")


# list comprehension
list = [x for x in "Geeks for Geeks"]
print(list)