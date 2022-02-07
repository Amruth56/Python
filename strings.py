# While accessing an index out of range will cause an  " INDEX ERROR "
# Only integers are allowed to be passed as an index
# Float or other types will cause  " TYPE ERROR "

# in python, updating or deletion of characters from a string is not allowed. This will cause an error as item assignment or item deletion from a String is not supported

# String is immutable, hence elements of a string cannot be changed once its been assigned. Only new strings can be reassigned to the same name

st1 = "Hello World"
st1[0] = "M"
# TYPE ERROR : "str" object does not support item assignment
print(f"The updated string is {st1}")

# we can just update the entire string
sr = "hello"
print(sr)
sr = "world"
print(sr)

# Deletion of a character
qw = "Hello"
print(qw)
del qw[2]
print(qw)  # TYPE ERROR

# Deleting Entire String
# Here we will get an error because as th entire string is deleted an is unavaliable to be printed
we = "Hello"
print(we)
del we
print(we)           # NameError: name 'we' is not defined


#                       USE OF SPLIT FUNCTION
txt="Welcome to bangalore"
print(f"the text after using slpit() function is \t {txt.split()}")


