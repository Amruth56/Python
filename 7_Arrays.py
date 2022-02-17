# Here we store multiple items of the same type together

# we can create array using array module, all the elements of the array must be of the same type.

# In python we can create an array by importing array module. array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.

import array as arr

a= arr.array('b',[1,2,3])
print("the newely created array is :", end=" ")
for i in range (0,3):
    print(a[i],end=' ')
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
# print("the newely created array is :", end=" ")
# for i in range (0,3):
#     print(a[i],end=' ')
# print()                                                                 
                #                                                       output= the newely created array is :
                #                                                               1
                #                                                               2
                #                                                               3