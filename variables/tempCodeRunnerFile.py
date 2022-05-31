# ALL:

# Illustration of 'all' function in python 3

# Take two lists
list1=[]
list2=[]

# All numbers in list1 are in form: 4*i-3
for i in range(1,21):
	list1.append(4*i-3)
print("/n", list1)
# list2 stores info of odd numbers in list1
for i in range(0,20):
	list2.append(list1[i]%2==1)
print("/n",list2)

print('See whether all numbers in list1 are odd =>')
print(all(list2))
