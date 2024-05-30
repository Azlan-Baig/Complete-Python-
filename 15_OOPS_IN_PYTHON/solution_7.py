class Car:
    def __init__(self,make,model):
        self.make = make
        self.__model=model
    
    @staticmethod    
    def generate_static():
        return "Cars are good"
     
     
my_car = Car("Toyota","Corolla")     
print(Car.generate_static())
print(my_car.make)
