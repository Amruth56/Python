# WHILE LOOP 

count = 0
while (count <=3):
    count = count +1 
    print ("NOC")

else:
    print("ELSE statement")


li= [1,2,3,4,5,6]
for i in range (len(li)):
    print(li[i],end=" ")

for letter in 'geeksforgeeks': 
    if letter == 'e' or letter == 's':
         continue
    print ('\nCurrent Letter :', letter)
    # var = 2

for letter in 'geeksforgeeks':
    
	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print ('Current Letter :', letter)
