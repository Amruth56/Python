def f():
    global s
    s += "gfg"
    print(s)
    s= "where are you now"
    print(s)

#Global variable
s= "King of court"
f()
print(s)