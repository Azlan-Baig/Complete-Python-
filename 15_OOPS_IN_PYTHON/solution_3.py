class Car:
    def __init__(self,make,model):
        self.make = make
        self.model=model
 
class Electric_Car(Car):        
    def __init__(self, make, model,battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
        

my_car = Electric_Car("Toyota","Corolla","20Kv")
print(my_car.battery_size)

