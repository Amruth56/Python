class item:
    def __init__(self) :
        print("Instance")

item1= item()  #python calls the init function 


class x:
    def __init__(self,name,price,year):
        print(f"An instance created : {name} of price {price}, which is manufactured in the year {year}")


a= x("Laptop",52000,2022)
b=x("Mobile",20000,2021)