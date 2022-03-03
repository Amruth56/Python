#           Tuples are immutable
tuple1=("apple","banana","Mango")
print(tuple1)
print("\n")

tuple2=tuple("banana")
print(tuple2)
print("\n")

tuple3=(1,2,3,4)
tuple4=tuple1,tuple3
print (tuple4)
print("\n")

for i in range (5):
    tuple1=tuple1,
    print(tuple1)

#                                       ACCESSING A TUPLE
print()
tuple1=tuple("hello")
print(tuple1[1])

tuple1=("apple","banana","Mango")
a,b,c=tuple1
print(f"\n values after unpacking are\t {a}, {b}, {c}")


#                                       CONCENTRATION OF TUPLES
#           Its a process of joining two or more tuples, its done by the use of + operator. Its always done at the end of original tuple and other arthematic operations do not apply in tuples.

tuple1=(1,2,3)
tuple2=("a","b","c")
print(f"\nconcentration of tuples {tuple1} and {tuple2} is {tuple1 + tuple2}")


#                                       SLICING OF TUPLE
tuple1=("quick work")
print(f"\n removal of 1st element {tuple1[1:]}")
print(f"\n reversing the tuple {tuple1[::-1]}")
print(f"\n slicing the tuple in between {tuple1[2:7]}")


#                                       DELETING THE TUPLE
# tuples are immutable and hence they do not allow deletion of a part of it. the entire tuple gets delted by the use of del() method

tuple1=(12,3,4)
del(tuple1)
print(tuple1)           #NAME ERROR AS tuple1 is not defined