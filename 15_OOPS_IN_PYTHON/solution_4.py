class Car:
    def __init__(self,make,model):
        self.make = make
        self.__model=model #  __ se ye private hugaya matlab within class to acces hosakta par is say object nahi ban sakta
    def get_brand(self):
        return self.__model  + " acccesible through getter"   
    def full_name(self):
        return f"{self.make} {self.__model}"    
    
mycar = Car("Toyota","Corolla")
print(mycar.full_name())
print(mycar.get_brand())
