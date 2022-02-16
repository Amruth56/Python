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
dict [0]="hello"
dict[1]=1
dict[2]=2
dict[3]=3
dict[4]="mic testing"
print(f"\nThe dictionary after adding 5 mixed elements is     {dict}")


