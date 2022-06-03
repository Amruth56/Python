def even_numbers(n):
    for num in n :
        if num%2==0:
            print("The list contains even numbers ")
            break

    else:
        print("The list contains only odd numbers")


print("For list 1")
even_numbers([1,2,3])
print("List 2")
even_numbers([1,3,5,7])


count=0
while (count<10):
    count=count+1
    print("Thr number is",count)
    # break
else:
    print("404")