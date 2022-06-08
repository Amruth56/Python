# __iter__() to access an object like an iterator
# it returns the iterator for the given object.
# it creates an object that creates one element at a time using __next__() function.


# SYNTAX

# iter(object) : the object whose iterator has to be created
# iter(callable,sentinel) : callable represents a callable object, and sentinel is the value at which the iteration is needed to be terminated.  

listA = ['a','e','i','o','u']
 
iter_listA = iter(listA)
print(iter_listA)