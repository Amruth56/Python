import operator as op

a=4
b=3

print("addition of two numbers a and b is ", op.add(a,b))
print("subtraction of two numbers a and b is ", op.sub(a,b))
print("multiplication of two numbers a and b is ", op.mul(a,b))
print("power of two numbers a and b is ", op.pow(a,b))
print("modulus of two numbers a and b is ", op.mod(a,b))


li = [1,2,3,4,5,6]
for i in range (0, len(li)):
    print(li[i],end=" ")

print("\n ")

op.setitem(li,3,73)  # position, number
for i in range (0, len(li)):
    print(li[i],end=" ")

# similarly for delitem, getitem