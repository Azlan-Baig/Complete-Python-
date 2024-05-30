class Car:
    car_count = 0
    def __init__(self,make,model):
        self.make = make
        self.model=model
        Car.car_count+=1

class Electric_Car(Car):        
    def __init__(self, make, model,battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

        
tesla = Electric_Car("Tesla","Etron","200 KWH")
toyota = Car("Toyota","Corolla")

print(Car.car_count)
