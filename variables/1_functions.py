# its declared using "DEF" keyword before the name of the function 

def division(a,b):
    if a%b==0:
        print("a is divisible by b")
    elif b%a==0:
        print("b divides a")
    else:
        print("a is not divisible by b")
division(4,4)

print(type(type(int)))


def f():
    s="King of hell"
    print("Inside function",s)
    print(s)
f()
# print(s)                    NameError : 's' is not defined