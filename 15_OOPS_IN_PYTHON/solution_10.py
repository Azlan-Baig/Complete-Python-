class Car:
    def __init__(self,make,model):
        self.make = make
        self.model=model
        
class Battery:
    def battery_info(self):
        return "This is battery"
class Engine:
    def Engine_info(self):
        return "This is Engine"

class Electric_car(Battery,Engine,Car):
    pass

mycar = Electric_car("Toyota","Corolla")
print(mycar.model)
print(mycar.battery_info())
print(mycar.Engine_info())
