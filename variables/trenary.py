# It evaluates something based on a condition of being true or false

# SYNTEX :                      [on_true] if [expression] else [on_false]

a,b=10,20
min = a if a<b else b 
print (min)

# ---------------------------------------------------------------------------------------

a,b = 20, 40
print("both a and b areequal " if a==b else "a is greater than b" if a>b else "b is greater than a ")

# ---------------------------------------------------------------------------------------

a= int(input())
b= int(input())

print("a==b" if a == b else "a>b" if a>b else "b >a")

# ---------------------------------------------------------------------------------------
a, b= 5,9
#       [starement_on_true]   if [statement] else [statement_on_false]
print( [a,"is greaterthan b"] if    (a>b)    else [b,"b is greater than a "] )

# ---------------------------------------------------------------------------------------

