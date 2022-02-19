# Here we store multiple items of the same type together

# we can create array using array module, all the elements of the array must be of the same type.

# In python we can create an array by importing array module. array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.

import array as arr

a= arr.array('b',[1,2,3])

# a= arr.array('b',[1,2,3])                               TypeError: array() argument 1 must be a unicode character, not list

print("the newely created array is :", end=" ")
for x in range (0,3):
    print(a[x],end=' ')
print()

#a= arr.array('b',[1,2,3])
# print("the newely created array is :", end=" ")
# for i in range (0,3):
#     print(a[i],end=' ')
# print()                                                                   
                 #                                                       output= the newely created array is :123


# a= arr.array('b',[1,2,3])
# print("the newely created array is :")
# for i in range (0,3):
#     print(a[i],end=' ')
# print()                                                                  
                 #                                                      output= the newely created array is :
                 #                                                            123


# a= arr.array('b',[1,2,3])
# print("the newely created array is :")
# for i in range (0,3):
#     print(a[i])
# print()                                                                 
                #                                                       output= the newely created array is :
                #                                                               1
                #                                                               2
                #                                                               3



                                        # ADDING ELEMENTS TO THE ARRAY
#we use built-in insert() function to insert elements to the array.
#append() is also used to add the value mentioned in its arguments at the end of the array.

import array as arr
a= arr.array('i',[1,2,3,4,5,6])
print("\nArray before inserting an element :", end=' ')
for x in range (0,6):
    print(a[x],end=' ')

a.insert(4,11)  #   (position, value)
print("\nArray after the insertion of 11 at the 4th position :", end=' ')
for x in a:
    print(x,end=' ')
print()

b=arr.array('d',[1.1, 2.2, 3.3])
print("Array before the append of any value :", end=' ')
for k in range (0,3):
    print(b[k],end=' ')
print()

b.append(4.4)
print("Array after the append of 4.4 is :", end=" ")
for x in b:
    print(x,end=" ")
print()


#                                       ACCESSING ELEMENTS FROM THE LIST
import array as arr
a=arr.array('i',[1,2,3,4,5,6,7])
print(f"\naccessing the elements from 1st position of the array :{a[1]}")


#                                       REMOVING ELEMENTS FROM THE ARRAY
import array as arr
a=arr.array('i',[1,2,3,4,5,6,6])
# print("\r")
print("\nThe popped element of the array is :",end=" ")
print(a.pop(2))

a.remove(6)                                                 #using remove function we can remove only 1 element at a time.
print("the array after removing is :",end=" ")
for i in range (0,5):
    print(a[i],end=" ")
print()


                                        # SLICING OF AN ARRAY
import array as arr
l=[1,2,3,4,5,6,7,8,9]
a=arr.array('i',l)
print("\nInitial array :",end=" ")
for i in  a:
    print(i,end=" ")
print()

print(f"slicing elements in the range 3-8 :{a[3:8]}")
print(f"printing an array backwards :{a[::-1]}")
print(f"Printing an element from specific point to end :{a[4:]}")


                                        # SEARCHING ELEMENTS IN AN ARRAY

import array as arr

a= arr.array("i",[1,2,3,4,5,6,7,8,9,10])
print("\nthe newely created array is :",end=" ")
for i in a :
    print(i,end=" ")
print(f"\nThe index of first occurenceof 6 is :{a.index(6)}")
print(f"The index of first occurenceof 1 is :{a.index(1)}")

#                                       UPDATING ELEMENTSIN AN ARRAY

import array as arr
a=arr.array("i",[1,2,3,4,5,6,7,8,9,10])
print("\nThe elements present in the array are :",end=" ")
for x in a:
    print(x,end=" ")
a[1]=22
print(f"\narray after updation :",end =" ")
for i in a:
    print(i,end=" ")
print()
