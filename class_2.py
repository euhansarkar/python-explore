class Car:
    def __init__(self, model):
        self.model = model 
    
    def __str__(self):
        return f"hello {self.model}"

car1 = Car("toyota")

# print(car1)

# print(car1.__str__)


class Mar:
    def __init__(self, model):
        self.model = model
    
    def __str__(self):
        return f"Car(model={self.model})"
    
mar1 = Mar("ferrari")

# print(mar1)



class Gar:
    def __init__(self, model):
        self.model = model 

    def __str__(self):
        return f"my car name is {self.model}"
    
gar1 = Gar("BMW")

print(gar1)

