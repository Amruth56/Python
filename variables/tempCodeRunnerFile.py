def f():
    global s
    s += "gfg"
    print("1",s)
    s = "gfg"
    print("1.1",s)
    s= "where are you now"
    print("2",s)

#Global variable
s= "King of court "
f()
print("3",s)