# Using enumerate():  enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.

for key, value in enumerate (["hello", "world", "its", "a", "new", "day"]):
    print(key,value)
print("\n")

for key, value in enumerate (["hello", "world", "its", "a", "new", "day"]):
    print(key,end=" ")
print("\n")

for key, value in enumerate (["hello", "world", "its", "a", "new", "day"]):
    print(value,end=" ")