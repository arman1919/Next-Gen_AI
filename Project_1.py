class Resource:
    def __init__(self,name:str,manufacturer:str,total:int,allocated:int) -> None:
        self._total = total
        self._allocated = allocated
        self._name = name
        self._manufacturer = manufacturer

    
    def __str__(self) -> str:
        return f" name - {self._name}"
    
    def __repr__(self) -> str:
        return f"name - {self._name} | manufacturer - {self._manufacturer} \ntotal = {self._total} | allocated = {self._allocated}  "
    
    
    
    def claim(self,n):
        if  self._total - n >= 0:
            self._total -= n
            self._allocated += n
            print(f"clamed {n} pieces")
        else:
            print("Low count")
    
    def freeup(self,n):
        if self._allocated - n >= 0:
            
            self._total += n
            self._allocated -= n
            print(f"freeup {n} pieces")
        else:
            print("low count")


    
    
    def died(self,n):
        if self._allocated - n >= 0:
            self._allocated -= n
            print (f"died {n} pieces")
    
    def purchased(self,n):
        self._total += n
        print(f"purchased {n} pieces")

    
    def Category(self):
        return self.__class__.__name__
    

class CPU(Resource):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int,core:int,interface:str,socket:str,power_watts:float) -> None:
        super().__init__(name, manufacturer, total, allocated)
        self.core = core
        self.interface = interface
        self.socket = socket
        self.power_watts = power_watts

class Storage(Resource):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int,capacity_GB:int) -> None:
        super().__init__(name, manufacturer, total, allocated)
        self.capacity_GB = capacity_GB

class HDD(Storage):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, capacity_GB: int,size:float,rpm:int) -> None:
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.size = size
        self.rpm  = rpm

class SSD(Storage):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, capacity_GB: int,interface:str) -> None:
        super().__init__(name, manufacturer, total, allocated, capacity_GB)



cpu = CPU("Pentium","Intel",5,0,5,"PCIe NMVe 3.0 x4","AM4",152.6)
hdd = HDD("F5","Kingston",2,0,256,2.5,7000)
ssd = SSD("K5","Samsung",3,0,512,"PCIe NMVe 3.0 x4")

cpu.claim(2)
ssd.freeup(1)
cpu.died(1)
hdd.purchased(2)
