# Using enumerate():  enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.

for key, value in enumerate (["hello", "world", "its", "a", "new", "day"]):
    print(key,value)
print("\n")

for key, value in enumerate (["hello", "world", "its", "a", "new", "day"]):
    print(key,end=" ")
print("\n")

for key, value in enumerate (["hello", "world", "its", "a", "new", "day"]):
    print(value,end=" ")

    # Using zip(): zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially. The loop exists only till the smaller container ends. 

que = ["name", "age", "native place", "gender"]
ans = ["Amruth", 20, "Kodagu", "Male"]

for q , a in zip (que, ans):
    print(f"what is your {q}? My {q} is= {a}")


# using items
# python code to demonstrate working of items()

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
		'Modi': 'The Changer'}

# using items to print the dictionary key-value pair
for i, j in king.items():
	print(i, j)

# Using sorted():  sorted() is used to print the container is sorted order. It doesn’t sort the container but just prints the container in sorted order for 1 instance. The use of set() can be combined to remove duplicate occurrences.

list = [1,1,2,5,3,4,6,7,5,6,9,7,8,9,76]

print("The list in sorted order =")
for i in sorted(list):
    print(i, end=" ")

print("\r")

print("To print in sorted order without any duplicates =")
for i in set(sorted(list)):
    print(i,end=" ")
print("\r")

print("To print the set in reversed order without any repetition")
for i in set(reversed(list)):
    print(i,end=" ")