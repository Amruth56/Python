# its unordered collection of data values . Dictionary holds KEY:VALUE pair
            # --- key in dictionary does not allow polymorphism 

#--- Dictionary keys are case sensitive, the same name but different case of key will be  treated distinctly.

#----> key:value     value in the dictionary can be of any data type and can be duplicate. where as keys must be immutable.

dict = {1:"hello",2:"world", 3:69, 5:[1,2,3,4,5]}
print(f"the newely created dictionary is \t{dict}")


#                                       ADDING ELEMENTS TO THE DICTIONMARY
dict ={}
print(f"\nIts an empty dictionary `{dict}")

#Adding elements to the empty dictionary
dict[0]="hello"
dict[1]=1
dict[2]=2
dict[3]=3
dict[4]="mic testing"
dict["a"]="XD"                  #alphabet --> key
print(f"\nThe dictionary after adding 5 mixed elements is     {dict}")


#                                       Accessing elements from the list
#--- in order to access the elements from a dictionary we make use of its key. Key can be used inside square brackets
dict={1:"hello", 2:"world", "smile":"good", 6:"morning"}
print(f"\nAccessing the elements from the list \t{dict[1]} {dict['smile']}")

#we can also make use of get() method.
print(f"Accessing the element from the list using get method \t{dict.get(6)}")


#                                       Accessing elements from the nested dictionary
dict={'dict1':{1:"hello", 2:[11,22,33,44,55]},
    'dict2':{'position':'king', 'kingdom':'SriLanka', 'name':'Ravana'},
    'dict3':["q","w","e","r","t","y"]}

print(f"\nAccessing elements from a nested dictionary \t{dict['dict1']}\t {dict['dict2']['name']}\t {dict['dict3'][0]}\t {dict['dict1'][2][0]}")
