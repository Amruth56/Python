for i in range(0,5):
    for i in range(0,i+1):
        print("*",end=" ")
    print("\r")

rows= int(input("Enter the number of rows :"))
for i in  range (rows):
    for j in range((i+1)*2):
        print("*",end=" ")
    print("\r")

# To print the numbers 
rows = int (input("Enter the number of rows :"))
for i in range(rows,0,-1):
    for j in range (i-1,0,-1):
        print(j, end=" ")
    print("\r")