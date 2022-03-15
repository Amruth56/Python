#Global variables are those which are not defined inside any functions and have a global scope 
#Local variables are those which are defined inside a function and its scope is limited to that function only.  
# local variables are accessible only inside the function in which it was initialized where as the global variables are accessible throughout the program and inside every function. 

def f():
    print("inside function",s)

# global variable
s="Dark king"
f()
print("Outer function",s)

# ------------------------------------------------------------------------------------------------------------------------------------------------

def f():
    s="Hello world"
    print(s)

# global variable
s="Hola"
f()
print("Outer function",s)

# -------------------------------------------------------------------------------------------------------------------------------------------------

def f():
    s="Hello world"
    print("1,",s)

s="Hola"
print("2,",s)                
f()
print("3, Outer function",s)