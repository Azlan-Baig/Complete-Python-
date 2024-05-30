class Car:
    def __init__(self,make,model):
        self.make = make
        self.__model=model
    
    @staticmethod    
    def generate_static():
        return "Cars are good"
    
    @property
    def Model(self):
        return self.__model
     
     
my_car = Car("Toyota","Corolla")     
print(my_car.Model)
