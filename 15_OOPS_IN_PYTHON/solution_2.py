class Car:
    def __init__(self,make,model):
        self.make = make
        self.model=model
    def full_name(self):
        return f"{self.make} {self.model}"    
    
    
    
    
my_car = Car("Toyota","Corolla")
print(my_car.full_name())