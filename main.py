from abc import ABC , abstractmethod
class Vehicale(ABC):
    @abstractmethod
    
    def getFuelType(self):
        pass
    def getMaxSpeed(self):
        pass
class BMW(Vehicale):
    def getFuelType(self):
        print("Premium Fuel")
    def getMaxSpeed(self):
        print("195 MPH")

class Ferrari(Vehicale):
    def getFuelType(self):
        print("Premium Fuel")
    def getMaxSpeed(self):
        print("249 MPH")

bmw = BMW()
print("Info about BMW : ")
bmw.getFuelType()
bmw.getMaxSpeed()
ferrari = Ferrari()
print("Info about Ferrari : ")
ferrari.getFuelType()
ferrari.getMaxSpeed()