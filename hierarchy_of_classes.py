from abc import ABC,abstractmethod

class Vehicl(ABC):
    object_class = "Vehicl"

    def __init__(self,price,color) -> None:
        self.price = price
        self.color = color

    @abstractmethod
    def to_ride(self):
        pass

    @abstractmethod
    def get_passenger_count(self):
        pass    


class Car(Vehicl):
    def __init__(self, price, color,door_count) -> None:
        super().__init__(price, color)
        self.door_count = door_count
    
    def to_ride(self):
        print("The car drives")

    def get_passenger_count(self):
        return 4
    
    def open_door(self):
        print("Door opend !")
        
class  Motorcycl(Vehicl):
    def __init__(self, price, color,helmet) -> None:
        super().__init__(price, color)
        self.helmet = helmet

    def to_ride(self):
        print("The motorcycl drives")
        
    def get_passenger_count(self):
        return 1
    
    def  Put_on_a_helmet(self):
        print("Put on your helmet")

class Bicycle (Vehicl):
    def __init__(self, price, color,pedals) -> None:
        super().__init__(price, color)
        self.pedals = pedals
    
    def to_ride(self):
        print("The bicycle drives")

    def get_passenger_count(self):
        return 0
    
    def pedaling(self):
        print("Pedaling")


car = Car(5000,"blue",4)
motorcycl = Motorcycl(2500,"Red","Monster")
bicycle = Bicycle(150,"black","P")

vehicls = [car,motorcycl,bicycle]

for vehicl in vehicls:
    vehicl.to_ride()
    print(vehicl.get_passenger_count())

    


