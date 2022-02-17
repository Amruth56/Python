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