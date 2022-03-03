# Set is an unordered collection of data that is iterable, mutable and has no duplicate elements 
# A set is highly optimized method for checking whether a specific element is contained in the set.

#                                       CREATING A SET
set1={1,2,3,4,5}
print(set1)
set2=set(["hello","world"])
print(set2)
set3=set("long college book")  # set are unordered, so they can be printed in any order
print(set3)


#                                       ADDING ELEMENTS TO THE SET
set1=set()
print(f"\ninitial set ={set1}")
set1.add(1)
set1.add(2)
set1.add(3)
print(f"set after adding 3 elements ={set1}")
for i in range(4,11):
    set1.add(i)
print(f"set1 after adding elements from 4 to 10 using for loop ={set1}")

#                   using update() method
# it is used to add two or more elements. It accepts list, tuple, strings as well as other sets and duplicate elements are avoided.

set1={1,2,3,4}
set1.update([10,3,"hello","King"])
print(f"set1 after update is ={set1}")


#                                       ACCESSING A SET
#   Sets cannot be accessed by refering to an index, since sets are unordered and have no index


#                                       REMOVING ELEMENTS FORM THE sET
#Using remove() method or discard() method
#           KEYERROR occurs if element doesn't exist in the set. To remove the elements from a set without key error, use discard(), if the element doesn't exist in the set it remains unchanged.
set1={1,2,3,4,5,6,7,8,9}
print(f"\n initial set1= {set1}")
set1.remove(1)
print(f"set1 after the removal of 1 from the original set= {set1}")
set1.discard(2)
print(f"set1 after the discard of 2 from set1= {set1}")
set1.discard(2)
print(f"set1 after the discard of already discarded number 2 from set1 ={set1}")

#use of pop amd() clear()
#pop only removes last element of the set and clear removes all the elements from the set
set1={1,2,3,4,5,6,7,8,9}
set1.pop()
print(f"elements in the list after using pop function ={set1}")
set1.clear()
print(f"elements in the list after using clear function ={set1}")