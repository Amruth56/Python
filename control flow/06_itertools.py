# count(start,step): iteration starts from the start number and prints in the steps mentioned 

import itertools

for i in itertools.count(5,5):
    if i == 105:
        break
    else:
        print(i,end=" ")
print("\n")
# cycle(iterable): This iterator prints all values in order from the passed container. It restarts printing from the beginning again when all elements are printed in a cyclic manner.

count = 0

for i in itertools.cycle("AM "):
    if count > 11:
        break
    else:
        print(i)
        count +=1
print ("\n")

# Python program to demonstrate
# infinite iterators

import itertools

l = ['Geeks', 'for', 'Geeks']

# defining iterator
iterators = itertools.cycle(l)

# for in loop
for i in range(6):
	
	# Using next function
	print(next(iterators), end = " ")
print("\n") 



# repeat(val, num): This iterator repeatedly prints the passed value an infinite number of times. If the optional keyword num is mentioned, then it repeatedly prints num number of times.

print("Printing the numbers repeatedly ")
print(tuple(itertools.repeat(5,6)))
