# its unordered collection of data values . Dictionary holds KEY:VALUE pair
            # --- key in dictionary does not allow polymorphism 

#----> Dictionary keys are case sensitive, the same name but different case of key will be  treated distinctly.

#----> key:value     value in the dictionary can be of any data type and can be duplicate. where as keys must be immutable.

dict = {1:"hello",2:"world", 3:69, 5:[1,2,3,4,5]}
print(f"the newely created dictionary is \t{dict}")


#                                       ADDING ELEMENTS TO THE DICTIONMARY
dict ={}
print(f"\nIts an empty dictionary `{dict}")

#Adding elements to the empty dictionary
dict[0]="hello"
dict[1]="one"
dict[2]=2
dict[3]=3
dict[4]="mic testing"
dict["a"]="XD"                  #alphabet --> key
print(f"\nThe dictionary after adding 5 mixed elements is     {dict}")


#                                       Accessing elements from the list
#--- in order to access the elements from a dictionary we make use of its key. Key can be used inside square brackets
dict={1:"hello", 2:"world", "smile":"good", 6:"morning"}
print(f"\nAccessing the elements from the list \t{dict[1]} \t{dict['smile']}")

#we can also make use of get() method.
print(f"Accessing the element from the list using get method \t{dict.get(6)}")


#                                       Accessing elements from the nested dictionary
dict={'dict1':{1:"hello", 2:[11,22,33,44,55]},
    'dict2':{'position':'king', 'kingdom':'SriLanka', 'name':'Ravana'},
    'dict3':["q","w","e","r","t","y"]}

print(f"\nAccessing elements from a nested dictionary \t{dict['dict1']}\n {dict['dict2']['name']}\n {dict['dict3'][0]}\n {dict['dict1'][2][0]}")



#                                       Removing elements from the dictionary

#---> most of the times deletion of key is done by the use of del keyword. Using the del keyword, specific values from the dictionary as well as the whole dictionary can be deleted. Items in a nested dictionary can also be deleted by using the del keyword and providing a specific nested key and particular key to be deleted from the nested Dictionary. 

dict = {1:"hello",2:"world", 3:69, 5:[1,2,3,4,5], 'dict1':{'position':'king', 'kingdom':'SriLanka', 'name':'Ravana'}}
print(f"\nInitial dictionary \t{dict}")

#deleting a key value
del dict[1]
print(f"Dictionary after deleting the eky value 1 from the dictionary \t{dict}")

#Deleting a key from Nested dictionary
del dict['dict1']['kingdom']
print(f"Dictionary after deleting a key from Nested Dictionary \t{dict}")


#                    USING POP() METHOD
#--- Used to del and return the value of the specific key
dict = {1:"hello",2:"world", 3:69, 5:[1,2,3,4,5], 'dict1':{'position':'king', 'kingdom':'SriLanka', 'name':'Ravana'}}
a=dict.pop(1)
print(f"\nThe dictionary after poping a key element \t{dict}")
print(f"The value associated vit the pop keyword is \t{a}")


#                    USING POPITEM()
#--- It returns and removes an arbitrary element{key:value} pair from the dictionary.
dict = {1:"hello",2:"world", 3:69, 5:[1,2,3,4,5], 'dict1':{'position':'king', 'kingdom':'SriLanka', 'name':'Ravana'}}
a=dict.popitem()                            #while using popitem always the last key:value pair gets popped 
print(f"\nThe dictionary after poping a key element \t{dict}")
print(f"The value associated with the popitem keyword is \t{a}")


#                   USING CLEAR() METHOD
#--- All the elements from the dictionary can be deleted at once after using clear() method

dict1 = {1:"hello",2:"world", 3:69, 5:[1,2,3,4,5], 'dict1':{'position':'king', 'kingdom':'SriLanka', 'name':'Ravana'}}
dict1.clear()
print("\nDeletion of entire dictionary")
print(dict1)
