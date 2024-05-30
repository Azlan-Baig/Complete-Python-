class Car:
    def __init__(self,make,model):
        self.make = make
        self.model=model
    def fuel_type(self):
        return "Petrol and Diesel"
class Electric_Car(Car):        
    def __init__(self, make, model,battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"   
        
tesla = Electric_Car("Tesla","Etron","200 KWH")
toyota = Car("Toyota","Corolla")

print(tesla.fuel_type())
print(toyota.fuel_type())
