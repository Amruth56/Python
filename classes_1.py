#Methods are the functions inside the classes
class Item:
    def total_price(self,x,y):
        return x*y


item1 = Item () # creating an instance of a class


 # CREATING AN ATTRIBUTE
item1.name="redmi"
item1.price= 11000
item1.quantity=5
print(item1.total_price(item1.price,item1.quantity))

item2=Item()
item2.name="samsung"
item2.price= 23000
item2.quantity=10
print(item2.total_price(item2.price,item2.quantity))

print(type(item1))
print(type(item1.name))
    