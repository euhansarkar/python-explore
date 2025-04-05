class Product:
    def __init__(self, name = "potato", price = 100):
        self.name = name 
        self.price = price 

    def __str__(self):
        return f"{self.name}'s price is {self.price}"

product1 = Product()

# print(product1)
# print(product1.name)
# print(product1.price)



class Sroduct:
    def __init__(self, name = "hello", price = 10):
        self.name = name 
        self.price = price 

    def __str__(self):
        return f"{self.name} has price {self.price}"
    
sroduct1 = Sroduct("world", 100)

# print(sroduct1)
# print(sroduct1.name)
# print(sroduct1.price)