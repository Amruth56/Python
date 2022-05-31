# ANY: Returns true if any of the items is True. It returns False if empty or all are false. It can also be used as an OR operator

print(any([True, False, True]))
print(any([False,False]))

# ALL: Returns true if all of the items are True (or if the iterable is empty). All can be thought of as a sequence of AND operations on the provided iterables.
print("\n")
print(all([True, False, True]))
print(all([False,False]))
print(all([True,True]))


# ANY :

# This code explains how can we
# use 'any' function on list
list1 = []
list2 = []

# Index ranges from 1 to 10 to multiply
for i in range(1,11):
	list1.append(4*i)
print("\n",list1)

# Index to access the list2 is from 0 to 9
for i in range(0,10):
	list2.append(list1[i]%5==0)
print(list2)

print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))


# ALL:

# Illustration of 'all' function in python 3

# Take two lists
list1=[]
list2=[]

# All numbers in list1 are in form: 4*i-3
for i in range(1,11):
	list1.append(4*i-3)
print("/n", list1)
# list2 stores info of odd numbers in list1
for i in range(0,10):
	list2.append(list1[i]%2==1)
print("/n",list2)

print('See whether all numbers in list1 are odd =>')
print(all(list2))
